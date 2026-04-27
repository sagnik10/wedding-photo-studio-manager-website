from django.apps import AppConfig


class PagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wedding_platform.pages"
    label = "pages"
    verbose_name = "Pages"

    def ready(self):
        try:
            import wedding_platform.pages.signals
        except ImportError:
            pass