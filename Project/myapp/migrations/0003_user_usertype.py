# Generated by Django 4.2.3 on 2023-07-28 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(default='buyer', max_length=100),
        ),
    ]
