# from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from pnl_index.models import PnlIndex

def regular_job():
    '''Переодичекий запус создания записи в БД'''
    scheduler = BackgroundScheduler()
    scheduler.add_job(PnlIndex.create_record, 'interval', seconds=10)
    scheduler.start() 

