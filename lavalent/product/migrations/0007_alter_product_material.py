# Generated by Django 4.1.1 on 2022-10-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(default='none', max_length=120, verbose_name='Материал'),
        ),
    ]
