# Generated by Django 4.2.10 on 2024-04-28 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0006_remove_size_name_size_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
