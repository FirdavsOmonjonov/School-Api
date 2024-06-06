from django.contrib import admin
from .models import Class, Teacher, Student

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'f_name', 'l_name', 'price', 'get_class_names')
    list_display_links = ('id', 'f_name')

    def get_class_names(self, obj):
        return ", ".join([cls.name for cls in obj.class_name.all()])

    get_class_names.short_description = 'Class Names'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'f_name', 'l_name', 'class_name')
    list_display_links = ('id', 'f_name')
