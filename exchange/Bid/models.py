from django.db import models


class Bid(models.Model):
    executor_id = models.BigIntegerField(verbose_name='Id исполнителя')
    customer_id = models.BigIntegerField(verbose_name='Id заказчика')
    description = models.CharField(max_length=4000, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
