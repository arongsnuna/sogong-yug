# Generated by Django 4.0.5 on 2022-06-21 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0008_alter_comment_clothes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='clothes',
        ),
    ]
