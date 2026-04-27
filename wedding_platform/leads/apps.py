from django.apps import AppConfig


class LeadsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wedding_platform.leads"
    label = "leads"
    verbose_name = "Leads"

    def ready(self):
        try:
            import wedding_platform.leads.signals
        except ImportError:
            pass