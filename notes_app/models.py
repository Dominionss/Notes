from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    reminder = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
