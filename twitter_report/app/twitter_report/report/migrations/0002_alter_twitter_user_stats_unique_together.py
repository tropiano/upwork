# Generated by Django 3.2.15 on 2022-09-26 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='twitter_user_stats',
            unique_together={('timestamp', 'user_id')},
        ),
    ]
