from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wedding_platform.core"
    label = "core"
    verbose_name = "Core"

    def ready(self):
        try:
            import wedding_platform.core.signals
        except ImportError:
            pass