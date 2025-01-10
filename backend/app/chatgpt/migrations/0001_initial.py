# Generated by Django 5.1.1 on 2024-10-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatgptAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatgpt_username', models.CharField(max_length=64, unique=True)),
                ('plan_type', models.CharField(max_length=32)),
                ('access_token', models.TextField()),
                ('session_token', models.TextField()),
                ('refresh_token', models.TextField()),
                ('remark', models.TextField(verbose_name='Remark')),
                ('created_time', models.IntegerField(blank=True, db_index=True, verbose_name='Created Time')),
                ('updated_time', models.IntegerField(blank=True, db_index=True, verbose_name='最后修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='ChatgptCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=32, unique=True)),
                ('remark', models.CharField(blank=True, max_length=128, verbose_name='Remark')),
                ('gpt_account_list', models.JSONField(default=list)),
            ],
        ),
    ]
