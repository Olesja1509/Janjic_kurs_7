# Generated by Django 4.2.7 on 2023-11-29 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='chat_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='ID бота в телеграме'),
        ),
    ]