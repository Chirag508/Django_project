# Generated by Django 5.1.3 on 2024-11-20 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_app', '0002_customer_data_updationdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateTime', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('auther', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
        ),
    ]
