from django.urls import path

from users.views import StudentListView, ClassesListView, AllStudents

app_name = 'main'

urlpatterns = [
    path('', AllStudents.as_view(), name='all-students'),
    path('class/', ClassesListView.as_view(), name='classes-list'),
    path('class/<int:pk>/', StudentListView.as_view(), name='students-list'),
]
