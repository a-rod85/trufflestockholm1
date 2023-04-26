from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.ImageField()
    mumber_of_persons = models.ImageField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        verbose_name = 'reservations'
        verbose_name_plural = 'reservations'

    def __str__(self) -> str:
        return self.name