# Generated by Django 3.2.3 on 2021-06-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='', editable=False, max_length=200, unique=True),
        ),
    ]
