# Generated by Django 5.1.5 on 2025-01-31 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='price_list',
            field=models.FileField(blank=True, null=True, upload_to='medial/price_lists/', verbose_name='Прайс-лист (Excel)'),
        ),
    ]
