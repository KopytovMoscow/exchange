from django.db import models


class Order(models.Model):
    order_id = models.BigIntegerField(verbose_name='Id заказа')
    executor_id = models.BigIntegerField(verbose_name='Id исполнителя')
    customer_id = models.BigIntegerField(verbose_name='Id заказчика')
    status = models.SmallIntegerField(verbose_name='Статус заказа')
    title = models.CharField(max_length=40, verbose_name='Название')
    description = models.CharField(max_length=4000, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'