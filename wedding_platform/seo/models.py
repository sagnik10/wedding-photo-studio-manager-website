from django.db import models


class SEO(models.Model):
    page_slug = models.CharField(max_length=200, unique=True)

    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "seo_meta"

    def __str__(self):
        return self.page_slug