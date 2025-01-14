# Generated by Django 5.1.4 on 2025-01-10 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_follow_created_at_alter_follow_followed_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={},
        ),
        migrations.AddField(
            model_name='notification',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.TextField(),
        ),
    ]