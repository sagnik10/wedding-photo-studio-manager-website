from django.contrib.sitemaps import Sitemap
from wedding_platform.pages.models import Page


class PageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Page.objects.all()

    def location(self, obj):
        return f"/{obj.slug}/"