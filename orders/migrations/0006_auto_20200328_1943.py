# Generated by Django 3.0.4 on 2020-03-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_pasta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasta',
            name='name',
            field=models.CharField(choices=[('A', 'Baked Ziti w/Mozzarella'), ('B', 'Baked Ziti w/Meatballs'), ('C', 'Baked Ziti w/Chicken')], max_length=1),
        ),
    ]
