# Generated by Django 3.0.7 on 2021-03-27 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210327_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=1),
        ),
    ]
