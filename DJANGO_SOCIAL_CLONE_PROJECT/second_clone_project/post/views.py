from django.shortcuts import render

# Create your views here.
# Post views.py

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from django.http import Http404
from django.urls import reverse_lazy

from braces.views import SelectRelatedMixin

from .models import Post

from django.contrib.auth import get_user_model
User = get_user_model()

class ListPost(SelectRelatedMixin, generic.ListView):
    model = Post
    select_related = ('user', 'group')

class UserPost(generic.ListView):
    model = Post
    template_name = 'post/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class DetailPost(generic.DetailView):
    model = Post
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin, generic.CreateView):
    fields = ('message', 'group')
    model = Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('post:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Post skasowany')
        return super().delete(*args, **kwargs)