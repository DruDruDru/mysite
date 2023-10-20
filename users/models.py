from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def get_absolute_url(self):
        return reverse('edit', args=[str(self.id)])

    def get_alternate_url(self):
        return reverse('delete', args=[str(self.id)])
