from django.views.generic import ListView, DetailView

from users.models import StudentModel, ClassModel


class ClassesListView(ListView):
    model = ClassModel
    template_name = 'classes.html'
    queryset = ClassModel.objects.order_by('number')
    context_object_name = 'classes'


class StudentListView(DetailView):
    model = ClassModel
    template_name = 'index.html'
    context_object_name = 'class'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.object.students.order_by('surname', 'name')
        return context


class AllStudents(ListView):
    model = StudentModel
    template_name = 'index.html'
    queryset = StudentModel.objects.order_by('surname', 'name')
    context_object_name = 'students'
