# Generated by Django 3.0.4 on 2020-04-10 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20200410_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regular_pizza',
            name='numToppings',
            field=models.IntegerField(choices=[(0, 'Cheese'), (1, '1'), (2, '2'), (3, '3'), (5, 'Special')]),
        ),
        migrations.AlterField(
            model_name='sicilian_pizza',
            name='numItems',
            field=models.IntegerField(choices=[(0, 'Cheese'), (1, '1'), (2, '2'), (3, '3'), (5, 'Special')]),
        ),
    ]
