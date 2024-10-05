from django.contrib import admin
from student.models import Student,Course

class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "lastname",)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "description",)


admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)

