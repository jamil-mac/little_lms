from django.contrib import admin

from users.models import ClassModel, StudentModel


@admin.register(ClassModel)
class ClassModelAdmin(admin.ModelAdmin):
    list_display = ['number']
    search_fields = ['number']
    list_filter = ['number']


@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    search_fields = ['name', 'surname']
    list_filter = ['name', 'surname']
