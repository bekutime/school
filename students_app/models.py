from courses_app.models import Course
from django.db import models

class Student(models.Model):
    GENDER_FEMALE = 'F'
    GENDER_MALE = 'M'

    GENDER_CHOICES = (
        (GENDER_FEMALE, 'Female'),
        (GENDER_MALE, 'Male'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField()
    phone_number = models.CharField(max_length=8)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-first_name']
        unique_together = (
            'first_name',
            'last_name',
            'phone_number',
            'email',

        )
    def __str__(self):
        return self.first_name


    def save(self, *args, **kwargs):
        for field_name in ['first_name','last_name']:
            val = getattr(self,field_name,False)
            if val:
                setattr(self,field_name,val.capitalize())
        super(Student,self).save(*args,**kwargs)
