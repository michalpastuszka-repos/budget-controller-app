# Generated by Django 4.1.3 on 2022-11-11 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0044_planyourexpanses'),
    ]

    operations = [
        migrations.AddField(
            model_name='planyourexpanses',
            name='amount_money_to_spent',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='How much money you want to spend to...'),
        ),
        migrations.AlterField(
            model_name='expensesinfo',
            name='expense_reason',
            field=models.CharField(choices=[('Rent', 'Rent'), ('Food', 'Food'), ('Fuel', 'Fuel'), ('Entertainment', 'Entertainment'), ('Other', 'Other'), ('Cosmetics and Chemicals', 'Cosmetics and Chemicals')], max_length=30),
        ),
        migrations.AlterField(
            model_name='planyourexpanses',
            name='expanse_plan_reason',
            field=models.CharField(choices=[('Rent', 'Rent'), ('Food', 'Food'), ('Fuel', 'Fuel'), ('Entertainment', 'Entertainment'), ('Other', 'Other'), ('Cosmetics and Chemicals', 'Cosmetics and Chemicals')], max_length=30),
        ),
    ]
