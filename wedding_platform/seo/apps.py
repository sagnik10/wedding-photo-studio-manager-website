from django.apps import AppConfig


class SeoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wedding_platform.seo"
    label = "seo"
    verbose_name = "SEO"

    def ready(self):
        try:
            import wedding_platform.seo.signals
        except ImportError:
            pass