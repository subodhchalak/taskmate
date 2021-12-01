from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TaskList(models.Model):
    task=models.CharField(max_length=300)
    done=models.BooleanField(default=False)
    owner=models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return (f"{self.task} - {self.done}")


    class Meta:
        ordering=['-id']