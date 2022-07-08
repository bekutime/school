from students_app.models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    #class Meta нужно ставить по умолчании он берет данные из обьекта и вставляет его сюда
    class Meta:
        model = Student
        fields = [ 'first_name','last_name','date_of_birth','phone_number','email','gender','course',]