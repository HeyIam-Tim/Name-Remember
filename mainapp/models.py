from django.db import models


class NameRemember(models.Model):
    name = models.CharField(max_length=255, null=True)
    contacts = models.CharField(max_length=255, null=True)
    how_met = models.TextField(max_length=2555, null=True)

    def __str__(self):
        return self.name




