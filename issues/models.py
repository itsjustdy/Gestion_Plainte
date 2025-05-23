from django.db import models
from django.contrib.auth.models import User

class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[
        ('new', 'Nouveau'),
        ('open', 'Ouvert'),
        ('in-progress', 'En cours'),
        ('resolved', 'Résolu'),
        ('closed', 'Fermé')
    ])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=20, default="Medium")

    def __str__(self):
        return self.title