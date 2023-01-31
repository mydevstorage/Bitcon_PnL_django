from django.db import models
from .services import *


class PnlIndex(models.Model):
    '''Хранине записей основного процесса'''
    btc_usd_price = models.DecimalField(max_digits=10, decimal_places=2)
    asset_price = models.DecimalField(max_digits=10, decimal_places=2)
    pnl_current = models.DecimalField(max_digits=10, decimal_places=2)
    pnl_total = models.DecimalField(max_digits=10, decimal_places=2)
    index_pnl = models.DecimalField(max_digits=3, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_record(cls):
        '''Создание записи в основную таблицу'''
        # Первая запись в БД
        # PnlIndex.objects.create(btc_usd_price=20000, asset_price=200000, pnl_current=0, index_pnl=1, pnl_total=0)
        # По условию задания количество btc константа
        BTC_AMOUTN = float(10.00)
        prev_object = PnlIndex.objects.last()
        asset_price_previous = float(prev_object.asset_price)
        index_pnl_previous = float(prev_object.index_pnl)
        # Получение стоимости btc через api
        btc_usd_price = get_api_data()
        asset_price = round(BTC_AMOUTN * btc_usd_price, 2)
        pnl_current = asset_price - asset_price_previous
        pnl_total = float(prev_object.pnl_total) + pnl_current
        index_pnl = round(((asset_price / asset_price_previous) * index_pnl_previous), 2)
        PnlIndex.objects.create(
                btc_usd_price = btc_usd_price,
                asset_price = asset_price,
                pnl_total = pnl_total,
                index_pnl = index_pnl,
                pnl_current=pnl_current,
        )
