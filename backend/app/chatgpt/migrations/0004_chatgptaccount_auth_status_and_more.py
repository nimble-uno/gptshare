# Generated by Django 5.1.1 on 2024-10-18 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt', '0003_alter_chatgptaccount_refresh_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatgptaccount',
            name='auth_status',
            field=models.BooleanField(default=True, verbose_name='Authorization status'),
        ),
        migrations.AlterField(
            model_name='chatgptaccount',
            name='remark',
            field=models.TextField(blank=True, null=True, verbose_name='Remark'),
        ),
    ]
