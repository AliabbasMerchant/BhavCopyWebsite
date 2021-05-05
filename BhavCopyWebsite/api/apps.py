from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    
    def ready(self):
        from apscheduler.schedulers.background import BackgroundScheduler
        from .bhavcopy import download_and_ingest, init_data
        init_data()
        
        scheduler = BackgroundScheduler()
        scheduler.add_job(download_and_ingest, 'cron', day_of_week='mon-fri', hour='18', minute='0')
        scheduler.start()
