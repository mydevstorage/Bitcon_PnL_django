# Generated by Django 3.2.16 on 2023-01-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnl_index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customperiod',
            name='profit_in_percent',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
