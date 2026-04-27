from django.db import models
from django.conf import settings


class ClientGallery(models.Model):
    title = models.CharField(max_length=255)

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="client_galleries"
    )

    password = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "client_galleries"

    def __str__(self):
        return self.title