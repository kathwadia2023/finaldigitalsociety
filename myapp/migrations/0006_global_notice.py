# Generated by Django 5.0.1 on 2024-02-08 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='global_notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('notice', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
    ]