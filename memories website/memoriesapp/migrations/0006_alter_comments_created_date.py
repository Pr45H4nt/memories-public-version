# Generated by Django 4.1 on 2022-09-12 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoriesapp', '0005_comments_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
