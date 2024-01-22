from django.db import models
from django.contrib.auth.models import User

# Create your models here. 

class Food(models.Model):
    name = models.CharField(max_length=100)
    carb = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name


class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

