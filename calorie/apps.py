from django.apps import AppConfig


class CalorieConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calorie'
    def ready(self): #new
        import calorie.signals #new
