import requests
import datetime



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
    start_date = form['start_date']
    start_time = form['start_time']
    end_date = form['end_date']
    end_time = form['end_time']
    created_previous = datetime.datetime.combine(start_date, start_time)
    created_next = datetime.datetime.combine(end_date, end_time)
    return created_previous , created_next














