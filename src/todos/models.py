from django.db import models

# Create your models here.
class Todo(models.Model):
    added_date = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.text