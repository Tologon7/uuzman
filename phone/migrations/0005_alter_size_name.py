# Generated by Django 4.2.10 on 2024-04-28 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0004_rename_state_size_remove_phone_state_phone_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.IntegerField(max_length=100),
        ),
    ]
