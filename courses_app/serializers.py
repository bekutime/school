from rest_framework.validators import UniqueTogetherValidator
#validators Один и тот же товар не будет добовлять
from courses_app.models import Course
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    #class Meta нужно ставить по умолчании он берет данные из обьекта и вставляет его сюда
    class Meta:
        model = Course
        fields = ['name','duration','price','is_active']

        #ТАКОЕ МОЖНО СДЕЛАТЬ ЕСЛИ С ФРОНТА БУДЕТ ПРИХОДИТЬ ИНФОРМАЦИЯ ЕСЛИ У ФРОНТА БУДЕТ МЕТОД POST
        #  Е
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Course.objects.all(),
        #         fields=['name','duration','price']
        #     )
        # ]
