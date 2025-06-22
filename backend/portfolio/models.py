from django.db import models

class Tattoo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name