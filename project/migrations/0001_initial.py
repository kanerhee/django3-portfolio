# Generated by Django 3.2 on 2021-06-04 21:27

from django.db import migrations, models
import martor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='project/images/')),
                ('url', models.URLField(blank=True)),
                ('date', models.DateField()),
                ('martorfield', martor.models.MartorField(blank=True, null=True)),
            ],
        ),
    ]