from django.views.generic import ListView

from users.models import StudentModel


class StudentListView(ListView):
    model = StudentModel
    template_name = 'index.html'
    queryset = StudentModel.objects.order_by('surname', 'name')
    context_object_name = 'students'
