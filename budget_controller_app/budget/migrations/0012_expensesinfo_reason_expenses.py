# Generated by Django 4.1.2 on 2022-10-16 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0011_expensesinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensesinfo',
            name='reason_expenses',
            field=models.CharField(choices=[('rent', 'rent'), ('food', 'food'), ('fuel', 'fuel'), ('entertainment', 'entertainment'), ('other', 'other')], default='', max_length=50),
        ),
    ]
