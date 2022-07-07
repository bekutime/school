from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    #PositiveIntegerField Выводит лишь плюсовые значения
    price = models.DecimalField(max_digits=8,decimal_places=2)
    #max_digits максимально число , decimal_places число послея запятой
    is_active = models.BooleanField(default=True)
    #BooleanField булевое значения

    class Meta:
        ordering = ['-name']
        unique_together = (
            'name',
            'duration',
            'price'

        )
    def __str__(self):
        return  self.name

