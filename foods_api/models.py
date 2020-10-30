from django.db import models

# Create your models here.
class Food(models.Model):
    food_id = models.TextField()

    def __str__(self):
        return self.food_id
