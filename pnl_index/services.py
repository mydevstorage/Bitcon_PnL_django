import requests
from  datetime import datetime


def get_api_data():
    '''Получение стоимость btc'''
    URL = ('https://test.deribit.com/api/v2/public/'
          'get_index_price?index_name=btc_usd')
    result = requests.get(URL)
    if result.status_code == 200:
        return float(result.json()['result']['index_price'])


def period_profit_in_percent(record_start, record_end):
    '''Рассчет прибыли в процентах'''
    result = ((float(record_end.index_pnl) /
               float(record_start.index_pnl)) - 1) * 100
    return round(result, 2)


def combine_date_and_time(form):
    '''Соединение даты и времени из формы'''
    prev = form['start_date'] + ' ' + form['start_time']
    next = form['end_date'] + ' ' + form['end_time']
    start_date = datetime.strptime(prev, '%Y-%m-%d %H:%M')
    end_date = datetime.strptime(next, '%Y-%m-%d %H:%M')
    return start_date , end_date


def handle_custom_period_request(form):
    from .models import PnlIndex
    from django.db.models import Q, Sum
    # Объединения даты и времени кастомного периода
    created_start, created_end = combine_date_and_time(form)
    # Выбираем ближайшие записи к выбранным датам
    object_start = PnlIndex.objects.filter(created__gte=created_start).first()
    object_end = PnlIndex.objects.filter(created__lte=created_end).last()
    # Условие, если непрравильный передается кастомныый период
    if not object_start or  not object_end:
        pnl_total, index_pnl, profit_in_prcnt, period = 0.0, 0.0, 0.0, 'wrong_period'
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
    result = {
        'pnl_total': pnl_total,
        'index_pnl': index_pnl,
        'profit_in_prcnt': profit_in_prcnt,
        'period': period,
    }
    return result











