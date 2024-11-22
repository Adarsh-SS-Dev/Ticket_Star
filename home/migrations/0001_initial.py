# Generated by Django 4.1.4 on 2023-03-09 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pic')),
                ('discount', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('screen', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=100)),
                ('pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film', to='home.film')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(max_length=100)),
                ('available', models.CharField(max_length=100)),
                ('sro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat', to='home.time')),
            ],
        ),
    ]