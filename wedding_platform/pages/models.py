from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    content = models.TextField()

    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "pages"
        ordering = ["-created"]

    def __str__(self):
        return self.title