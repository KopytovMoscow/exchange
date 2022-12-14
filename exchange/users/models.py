from django.db import models
from Skill.models import Skill
from Order.models import Order
from Bid.models import Bid


class Users(models.Model):
    # Пользовательская информация
    username = models.CharField(max_length=150, verbose_name='Короткое имя')  # Короткое имя пользвотаеля
    name = models.CharField(max_length=150, verbose_name='Имя')
    surname = models.CharField(max_length=150, verbose_name='Фамилия')

    # Служебная информация
    status = models.CharField(max_length=150, verbose_name='Статус')  # Статус пользователя: user, moderator, admin
    orders = models.ManyToManyField(Order)  # Строка, в которой зранятся ID заказов
    bids = models.ManyToManyField(Bid)  # ID заявок
    skills = models.ManyToManyField(Skill)  # ID карточек

    def __str__(self):
        return

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
