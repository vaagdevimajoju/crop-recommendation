from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    vitamins = models.CharField(max_length=200)
    benefits = models.TextField()
    disease_cure = models.TextField()
    fertilizers = models.TextField()
    expected_yield = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name