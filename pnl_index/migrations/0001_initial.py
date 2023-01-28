# Generated by Django 3.2.16 on 2023-01-28 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnl_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('profit_in_percent', models.DecimalField(decimal_places=2, max_digits=3)),
                ('index_pnl', models.DecimalField(decimal_places=2, max_digits=3)),
                ('period', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PnlIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc_usd_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('asset_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pnl_current', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pnl_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('index_pnl', models.DecimalField(decimal_places=2, max_digits=3)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]