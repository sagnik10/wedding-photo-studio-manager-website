from django.db import models


class CrawlTarget(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    region = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.region})"


class CrawlResult(models.Model):
    target = models.ForeignKey(CrawlTarget, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=True)
    meta_description = models.TextField(blank=True)
    h1_tags = models.TextField(blank=True)
    images = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.target.name} - {self.created_at}"