# Generated by Django 4.2.10 on 2024-04-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0005_alter_size_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='size',
            name='name',
        ),
        migrations.AddField(
            model_name='size',
            name='title',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
