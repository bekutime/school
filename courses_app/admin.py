from django.contrib import admin
from courses_app.models import Course
from students_app.models import Student


admin.site.register(Course)
admin.site.register(Student)
