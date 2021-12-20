from django.db import models

class Diagnosis(models.Model):
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.description