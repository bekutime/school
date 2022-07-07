from courses_app.models import Course
from courses_app.serializers import CourseSerializer
from rest_framework import viewsets
# Мы из rest_framework импортируем

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """information about courses Даем информацию фронтеншикам"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer