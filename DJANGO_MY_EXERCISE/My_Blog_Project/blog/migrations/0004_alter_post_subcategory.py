# Generated by Django 3.2.3 on 2021-06-05 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_subcategory_main_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.subcategory'),
        ),
    ]
