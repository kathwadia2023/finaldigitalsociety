# Generated by Django 5.0.1 on 2024-02-07 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_complaint_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]
