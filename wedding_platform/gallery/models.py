from django.db import models
from django.conf import settings


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="galleries"
    )

    is_private = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "galleries"
        ordering = ["-created"]

    def __str__(self):
        return self.title


class Photo(models.Model):
    gallery = models.ForeignKey(
        Gallery,
        related_name="photos",
        on_delete=models.CASCADE
    )

    image = models.ImageField(upload_to="gallery/photos/")
    caption = models.CharField(max_length=255, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "photos"
        ordering = ["-created"]

    def __str__(self):
        return self.caption or f"Photo {self.id}"