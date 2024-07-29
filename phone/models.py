from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Phone(models.Model):
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name='Тип товара')
    title = models.CharField(max_length=30, verbose_name='Название')
    content = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Изображение')
    price = models.FloatField(verbose_name='Цена (с)')
    quantity = models.IntegerField(verbose_name='Количество', default=1)
    size = models.ForeignKey('Size', on_delete=models.PROTECT, verbose_name='Размер')
    tel = models.IntegerField(verbose_name='Номер телефона', default=996700909915, blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовать')

    def __str__(self):
        return self.title
