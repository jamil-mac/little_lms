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
    context_object_name = 'students'

    def get_queryset(self):
        brilliant_student = StudentModel.objects.order_by('-brilliant_coin').first()
        ruby_student = StudentModel.objects.order_by('-ruby_coin').first()
        gold_student = StudentModel.objects.order_by('-gold_coin').first()
        iht_student = StudentModel.objects.order_by('-iht_coin').first()

        top_students = {brilliant_student, ruby_student, gold_student, iht_student}

        other_students = StudentModel.objects.exclude(id__in=[s.id for s in top_students]).order_by('surname', 'name')

        return list(top_students) + list(other_students)
