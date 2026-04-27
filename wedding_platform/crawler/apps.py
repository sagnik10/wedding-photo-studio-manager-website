from django.apps import AppConfig


class CrawlerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wedding_platform.crawler"
    label = "crawler"
    verbose_name = "Crawler"

    def ready(self):
        try:
            import wedding_platform.crawler.signals
        except ImportError:
            pass