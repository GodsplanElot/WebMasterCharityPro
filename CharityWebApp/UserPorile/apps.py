from django.apps import AppConfig


class UserporileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'UserPorile'

    def ready(self):
        import UserPorile.signals
