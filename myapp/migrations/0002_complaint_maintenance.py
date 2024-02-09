# Generated by Django 5.0.1 on 2024-02-06 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('complaint', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=20)),
                ('issue', models.CharField(max_length=20)),
                ('my_files', models.FileField(upload_to='Complaint_files')),
                ('comments', models.TextField()),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('wing', models.CharField(max_length=20)),
                ('block', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=20)),
                ('month', models.DateField()),
                ('my_files', models.FileField(upload_to='payment')),
            ],
        ),
    ]
