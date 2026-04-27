from django.db import models


class Lead(models.Model):
    STATUS_NEW = "new"
    STATUS_CONTACTED = "contacted"
    STATUS_CONVERTED = "converted"

    STATUS_CHOICES = [
        (STATUS_NEW, "New"),
        (STATUS_CONTACTED, "Contacted"),
        (STATUS_CONVERTED, "Converted"),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField(blank=True)

    score = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NEW,
    )

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "leads"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name} ({self.status})"