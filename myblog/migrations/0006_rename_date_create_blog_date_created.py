# Generated by Django 3.2 on 2021-04-27 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_alter_blog_date_create'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='date_create',
            new_name='date_created',
        ),
    ]