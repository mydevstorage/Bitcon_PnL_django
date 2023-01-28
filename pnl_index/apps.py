from django.apps import AppConfig

class PnlIndexConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pnl_index'

    def ready(self):
        import scheduler_jobs
        scheduler_jobs.regular_job()
