# Generated by Django 5.1 on 2024-09-04 04:28

import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
import web.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(null=True, verbose_name='Широта')),
                ('longitude', models.FloatField(null=True, verbose_name='Долгота')),
                ('city', models.CharField(max_length=30, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house', models.CharField(blank=True, max_length=20, null=True, verbose_name='Дом')),
                ('source', models.CharField(max_length=255, verbose_name='Полный адрес')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='advantage/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Преимущество',
                'verbose_name_plural': 'Преимущества',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='OrderOnline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('user_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Контактный телефон заказчика')),
                ('budget', models.CharField(choices=[('ONE_MILLION', 'До 1 млн'), ('ONE_THREE', '1-3 млн'), ('THREE_FIVE', '3-5 млн'), ('TEN_MILLION', 'до 10 млн')], max_length=20, verbose_name='Бюджет')),
            ],
            options={
                'verbose_name': 'Онлайн заявка',
                'verbose_name_plural': 'Онлайн заявки',
            },
        ),
        migrations.CreateModel(
            name='OrderPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Контактный телефон заказчика')),
                ('convenient_time', models.CharField(choices=[('QUICKLY', 'Как можно скорее'), ('IN_HOUR', 'Через час'), ('EVENING', 'Вечером'), ('TOMORROW', 'Завтра')], max_length=20, verbose_name='Удобное время звонка')),
            ],
            options={
                'verbose_name': 'Заказ звонка',
                'verbose_name_plural': 'Заказы звонка',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('sequence', models.PositiveIntegerField(default=0, unique=True, verbose_name='Порядок вывода')),
                ('image', models.ImageField(upload_to='partners/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
                'ordering': ('sequence',),
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='specializations/')),
            ],
            options={
                'verbose_name': 'Специализация',
                'verbose_name_plural': 'Специализации',
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='technologies/')),
            ],
            options={
                'verbose_name': 'Технология',
                'verbose_name_plural': 'Технологии',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, unique=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Работа',
                'verbose_name_plural': 'Работы',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Контактный телефон заказчика')),
                ('status', models.CharField(choices=[('HIRED', 'Принят в работу'), ('COMPLETED', 'Закрыт'), ('REJECTED', 'Отклонен'), ('WAITING', 'Ожидает решения')], default='WAITING', max_length=20, verbose_name='Статус заказа')),
                ('order_online', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.orderonline', verbose_name='Онлайн заявка')),
                ('order_phone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.orderphone', verbose_name='Заказ звонка')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Описание')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Порядок')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0), web.models.is_nan_validator], verbose_name='Цена услуги')),
                ('works', models.ManyToManyField(related_name='services', to='web.work', verbose_name='Перечень работ')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(help_text='Пример: +7 XXX XXX-XX-XX', max_length=128, region=None, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('telegram', models.CharField(max_length=255, verbose_name='Ссылка на телеграм')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.address', verbose_name='Адресс')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Котнтакты',
                'unique_together': {('phone', 'address')},
            },
        ),
    ]
