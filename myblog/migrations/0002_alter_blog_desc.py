# Generated by Django 3.2 on 2021-04-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='desc',
            field=models.TextField(),
        ),
    ]
