# Generated by Django 4.2.10 on 2024-07-29 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
                ('price', models.FloatField(verbose_name='Цена (с)')),
                ('quantity', models.IntegerField(default=1, verbose_name='Количество')),
                ('tel', models.IntegerField(blank=True, default=996700909915, max_length=12, null=True, verbose_name='Номер телефона')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовать')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='phone.category', verbose_name='Тип товара')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='phone.size', verbose_name='Размер')),
            ],
        ),
    ]
