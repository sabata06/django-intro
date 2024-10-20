from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    # joined = models.DateTimeField(auto)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # image =

    def __str__(self):
        return f"{self.first_name} {self.last_name} # {self.number}"

    class Meta:
        verbose_name = "Öğrenci"
        verbose_name_plural = "Öğrenciler"
        ordering = ["number"]
