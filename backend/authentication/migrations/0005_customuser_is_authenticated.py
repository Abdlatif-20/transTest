# Generated by Django 4.2.16 on 2024-10-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_customuser_avatar_url_customuser_tournament_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
    ]
