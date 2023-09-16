from django.db import models

# Create your models here.

class todolist(models.Model):
    text = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    
    # return a text representation of the content of the database
    def __str__(self):
        return self.text
    