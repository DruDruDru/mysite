# Generated by Django 4.2.6 on 2023-10-16 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_voted',
            field=models.BooleanField(default=False),
        ),
    ]
