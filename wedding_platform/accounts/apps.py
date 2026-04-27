from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wedding_platform.accounts"
    label = "accounts"
    verbose_name = "Accounts"

    def ready(self):
        try:
            import wedding_platform.accounts.signals
        except ImportError:
            pass