# Generated by Django 3.2 on 2021-04-20 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210420_0714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='question_type',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='trueAndfalse',
        ),
    ]
