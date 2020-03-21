from django.db import models


class Client(models.Model):
    """Data model for the client users"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
