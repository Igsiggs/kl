# Generated by Django 5.1.5 on 2025-01-31 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
                'default_related_name': 'category',
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Регион')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Наименование компании')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Сайт компании')),
                ('price_list', models.FileField(blank=True, null=True, upload_to='price_lists/', verbose_name='Прайс-лист (Excel)')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Поставщика',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование товара')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('bulk_price', models.IntegerField(verbose_name='Цена от 1000 кг')),
                ('implementation_period', models.CharField(max_length=100, verbose_name='Срок реализации')),
                ('weight_unit', models.CharField(max_length=10, verbose_name='Мера измерения')),
                ('is_new', models.BooleanField(default=False, verbose_name='Новинка')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products_image/', verbose_name='Картинка товара')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='products.category', verbose_name='Категория')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.supplier', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='products.supplier', verbose_name='Поставщик'),
        ),
    ]
