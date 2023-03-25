from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=256)
    ingredients = models.CharField(max_length=1024)
    picture = models.FileField()
    steps = models.TextField()

    def __str_(self):
        return "Recipe for {}".format(self.name)
