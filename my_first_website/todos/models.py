from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=80, default="New Title")
    content = models.TextField(max_length=500)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
