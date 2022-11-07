# Generated by Django 4.1.2 on 2022-11-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0033_alter_expensesinfo_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensesinfo',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Amount of expanse'),
        ),
        migrations.AlterField(
            model_name='income',
            name='income',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Amount income'),
        ),
    ]