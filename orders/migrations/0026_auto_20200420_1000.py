# Generated by Django 3.0.4 on 2020-04-20 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_auto_20200416_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sicilian_pizza',
            old_name='numItems',
            new_name='numToppings',
        ),
        migrations.AlterUniqueTogether(
            name='sicilian_pizza',
            unique_together={('numToppings', 'type')},
        ),
    ]