from django.db import models


class Skill(models.Model):
    # TODO: Переделать owner_id в foreign_key
    owner_id = models.BigIntegerField(verbose_name='Id Исполнителя')
    title = models.CharField(max_length=40, verbose_name='Название услуги')
    description = models.CharField(max_length=4000, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    currency = models.CharField(max_length=20, verbose_name='Валюта')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    likes = models.IntegerField(default=0, verbose_name='Отметка нравится')

    class Meta:
        verbose_name = 'Карточка услуги'
        verbose_name_plural = 'Карточки услуг'

