# Generated by Django 3.2.2 on 2021-05-14 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_firstname', models.CharField(max_length=254)),
                ('user_lastname', models.CharField(max_length=254)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
