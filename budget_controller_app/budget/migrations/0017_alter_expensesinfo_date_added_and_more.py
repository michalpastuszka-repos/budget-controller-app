# Generated by Django 4.1.2 on 2022-10-31 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0016_alter_expensesinfo_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensesinfo',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2022, 10, 31, 20, 55, 5, 745080)),
        ),
        migrations.AlterField(
            model_name='income',
            name='date_income',
            field=models.DateField(default=datetime.datetime(2022, 10, 31, 20, 55, 5, 744079)),
        ),
    ]
