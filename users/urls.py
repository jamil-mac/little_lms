from django.urls import path

from users.views import StudentListView

app_name = 'main'

urlpatterns = [
    path('', StudentListView.as_view(), name='students-list'),
]
