# Generated by Django 4.2.10 on 2024-04-28 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0003_state_alter_phone_price_alter_phone_tel_phone_state'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='State',
            new_name='Size',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='state',
        ),
        migrations.AddField(
            model_name='phone',
            name='size',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='phone.size', verbose_name='Размер'),
            preserve_default=False,
        ),
    ]
