# Generated by Django 4.0 on 2021-12-18 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=150)),
                ('ano', models.IntegerField()),
                ('marca', models.CharField(max_length=100)),
            ],
        ),
    ]