from djmoney.money import Money
from djmoney.models.fields import MoneyField

from django.db import models


class Work(models.Model):
    text = models.TextField('Описание')

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return self.text


class Service(models.Model):
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField('Slug', max_length=255, unique=True, db_index=True)
    description = models.TextField('Описание')
    order = models.SmallIntegerField('Порядок', default=0)
    works = models.ManyToManyField(Work, related_name='services', verbose_name='Перечень работ')
    price = MoneyField('Цена услуги', max_digits=14, decimal_places=2, default_currency='RUB',
                       default=Money(0, 'RUB'))

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ('order', )
