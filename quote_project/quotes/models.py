from django.db import models


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.author