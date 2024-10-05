from django.urls import path 
from student.views import list_students_view

urlpatterns = [
    path('list_students',view=list_students_view)
]