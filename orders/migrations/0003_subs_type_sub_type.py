# Generated by Django 3.0.4 on 2020-03-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_subs_type_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='subs_type',
            name='sub_type',
            field=models.CharField(choices=[('S', 'Small'), ('L', 'Large')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
