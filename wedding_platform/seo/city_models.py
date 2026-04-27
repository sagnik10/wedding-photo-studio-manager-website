from django.db import models


class CityPage(models.Model):
    city = models.CharField(max_length=100, db_index=True)

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "city_pages"
        ordering = ["city"]

    def __str__(self):
        return f"{self.city} Page"