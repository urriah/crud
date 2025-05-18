from django.db import models

class Build(models.Model):
    name = models.CharField(max_length=255)
    components = models.JSONField()  # Use TextField if not on Django 3.1+
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated']
        