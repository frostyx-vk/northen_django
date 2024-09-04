from phonenumber_field.modelfields import PhoneNumberField

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


def is_nan_validator(value):
    import math
    if math.isnan(value):
        raise ValidationError('Недопустимое значение поля. Поле не может быть NaN')


class Specialization(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='specializations/')

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField('Название', max_length=255)
    image = models.ImageField(upload_to='technologies/')

    class Meta:
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'

    def __str__(self):
        return self.name


class Work(models.Model):
    text = models.CharField('Описание', max_length=255, unique=True)

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
    price = models.FloatField('Цена услуги', validators=[MinValueValidator(0), is_nan_validator])

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ('order', )


class Advantage(models.Model):
    title = models.CharField('Заголовок', max_length=255, unique=True)
    text = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='advantage/')

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
        ordering = ('id', )

    def __str__(self):
        return self.title


class Address(models.Model):
    latitude = models.FloatField(verbose_name='Широта', null=True)
    longitude = models.FloatField(verbose_name='Долгота', null=True)
    city = models.CharField(verbose_name='Город', max_length=30)
    street = models.CharField(verbose_name='Улица', max_length=100)
    house = models.CharField(verbose_name='Дом', max_length=20, null=True, blank=True)
    source = models.CharField(verbose_name='Полный адрес', max_length=255)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'{self.city} {self.street} {self.house}'

    @property
    def p_latitude(self):
        return str(self.latitude).replace(',', '.')

    @property
    def p_longitude(self):
        return str(self.longitude).replace(',', '.')


class ContactInfo(models.Model):
    phone = PhoneNumberField('Номер телефона', help_text='Пример: +7 XXX XXX-XX-XX')
    email = models.EmailField('Электронная почта')
    telegram = models.CharField('Ссылка на телеграм', max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Адресс')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Котнтакты'
        unique_together = (('phone', 'address'), )

    def __str__(self):
        return f'{self.address} - {self.phone}'


class OrderPhone(models.Model):
    class ConvenientTime(models.TextChoices):
        QUICKLY = 'QUICKLY', 'Как можно скорее'
        IN_HOUR = 'IN_HOUR', 'Через час'
        EVENING = 'EVENING', 'Вечером'
        TOMORROW = 'TOMORROW', 'Завтра'

    user_phone = PhoneNumberField('Контактный телефон заказчика')
    convenient_time = models.CharField('Удобное время звонка', max_length=20, choices=ConvenientTime.choices)

    class Meta:
        verbose_name = 'Заказ звонка'
        verbose_name_plural = 'Заказы звонка'

    def __str__(self):
        return f'{self.user_phone.as_e164} - {self.convenient_time}'


class OrderOnline(models.Model):
    class Budget(models.TextChoices):
        ONE_MILLION = 'ONE_MILLION', 'До 1 млн'
        ONE_THREE = 'ONE_THREE', '1-3 млн'
        THREE_FIVE = 'THREE_FIVE', '3-5 млн'
        TEN_MILLION = 'TEN_MILLION', 'до 10 млн'

    description = models.TextField('Описание')
    user_phone = PhoneNumberField('Контактный телефон заказчика')
    budget = models.CharField('Бюджет', max_length=20, choices=Budget.choices)

    class Meta:
        verbose_name = 'Онлайн заявка'
        verbose_name_plural = 'Онлайн заявки'

    def __str__(self):
        return f'{self.budget} - {self.user_phone}'


class Order(models.Model):
    class Statuses(models.TextChoices):
        HIRED = 'HIRED', 'Принят в работу'
        COMPLETED = 'COMPLETED', 'Закрыт'
        REJECTED = 'REJECTED', 'Отклонен'
        WAITING = 'WAITING', 'Ожидает решения'

    user_phone = PhoneNumberField('Контактный телефон заказчика')
    order_phone = models.ForeignKey(OrderPhone, on_delete=models.CASCADE, verbose_name='Заказ звонка',
                                    blank=True, null=True)
    order_online = models.ForeignKey(OrderOnline, on_delete=models.CASCADE, verbose_name='Онлайн заявка',
                                     blank=True, null=True)
    status = models.CharField('Статус заказа', max_length=20, choices=Statuses.choices, default=Statuses.WAITING)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.order_phone} - {self.status}'


class Partner(models.Model):
    name = models.CharField('Название', max_length=255)
    sequence = models.PositiveIntegerField('Порядок вывода', unique=True, default=0)
    image = models.ImageField('Изображение', upload_to='partners/')

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
        ordering = ('sequence', )

    def __str__(self):
        return self.name