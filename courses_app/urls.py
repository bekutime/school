from django.urls import path, include
from courses_app.views import CourseViewSet

# as_view Зачем он нужен? он нужен что бы он запустился
urlpatterns = [
    path('', CourseViewSet.as_view({'get':'list'}), name = 'course-list'),
]