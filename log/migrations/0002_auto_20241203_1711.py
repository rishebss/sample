# Generated by Django 3.1.12 on 2024-12-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
