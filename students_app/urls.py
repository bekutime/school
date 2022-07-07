from django.urls import path, include
from students_app.views import StudentViewSet

# as_view Зачем он нужен? он нужен что бы он запустился
urlpatterns = [
    path('', StudentViewSet.as_view({'get':'list'}), name = 'student-list'),
]