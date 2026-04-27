from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wedding_platform.payments"
    label = "payments"
    verbose_name = "Payments"

    def ready(self):
        try:
            import wedding_platform.payments.signals
        except ImportError:
            pass