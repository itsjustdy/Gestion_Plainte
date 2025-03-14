from django.db import models
from django.contrib.auth.models import User

class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[('open', 'Open'), ('closed', 'Closed')])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title