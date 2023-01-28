from django.db import models
from .services import *
from django.db.models import Q, Sum



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




class CustomPeriod(models.Model):
    '''Для записи кастомных значений периода'''
    pnl_total = models.DecimalField(max_digits=10, decimal_places=2)
    profit_in_percent = models.DecimalField(max_digits=5, decimal_places=2)
    index_pnl = models.DecimalField(max_digits=3, decimal_places=2)
    period = models.CharField(max_length=250)

    @classmethod
    def create_custom_record(cls, form):
        '''Метод сохраняет обработанные данные, которые переданны из формы'''
        # Объединения даты и времени кастомного периода
        created_start, created_end = combine_date_and_time(form)
        # Выбираем ближайшие записи к выбранным датам
        object_start = PnlIndex.objects.filter(created__gte=created_start).first()
        object_end = PnlIndex.objects.filter(created__lte=created_end).last()
        # Условие, если непрравильный передается кастомныый период
        if not object_start or  not object_end:
            pnl, profit_in_prcnt, period = 0.0, 0.0, 'wrong_period'
        else:
            # Запрос для суммирование всех выбранных pnl за период
            pnl = (PnlIndex.objects.values('created', 'pnl_current')
            .filter(Q(created__gte=created_start),
            Q(created__lte=created_end)).aggregate(Sum('pnl_current')))
            pnl_total = float(pnl['pnl_current__sum']) if pnl['pnl_current__sum'] else 0
            index_pnl = round(((object_end.asset_price / object_start.asset_price) * object_start.index_pnl), 2)
            profit_in_prcnt=period_profit_in_percent(object_start, object_end)
            # Вывод кастомного периода
            period = (f'{created_start.strftime("%d.%m.%Y [%H:%M]")} - '
                      f'{created_end.strftime("%d.%m.%Y [%H:%M]")}')
        # Создание записи в БД
        # CustomPeriod.objects.create(pnl_total=20985.2, profit_in_percent=15.0, period='2022', index_pnl=1.15)
        CustomPeriod.objects.create(
            pnl_total=pnl_total,
            profit_in_percent=profit_in_prcnt,
            period=period,
            index_pnl=float(index_pnl),
        )
    








