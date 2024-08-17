from django.contrib import admin

from .models import Student, Teacher


class MemberTeacherInline(admin.TabularInline):
    model = Student.teachers.through


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [MemberTeacherInline, ]
    exclude = ('teachers',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [MemberTeacherInline, ]