# Generated by Django 4.2.16 on 2024-10-14 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_customuser_current_xp_customuser_friends_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar_url',
            field=models.ImageField(default='avatars/default.png', upload_to='avatars/'),
        ),
    ]
