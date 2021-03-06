# Generated by Django 3.0.4 on 2020-04-10 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20200410_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinner_platters',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='pasta',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='salads',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='sicilian_pizza',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='subs',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
