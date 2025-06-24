from django.db import models

# Create your models here.

class Tarefa(models.Model):
    title = models.CharField(max_length=200)
    isCompleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + '|' + str(self.isCompleted) + '|' + str(self.created_at.strftime("%Y/%m/%d %H:%M:%S"))
