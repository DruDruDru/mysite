# Generated by Django 4.2.6 on 2023-10-16 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_alter_choice_voted_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='voted_by',
        ),
    ]
