# Generated by Django 4.1.2 on 2022-10-31 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0015_rename_expense_name_expensesinfo_expense_reason_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensesinfo',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='expensesinfo',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2022, 10, 31, 19, 39, 19, 468822, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='date_income',
            field=models.DateField(default=datetime.datetime(2022, 10, 31, 19, 39, 19, 467823, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]