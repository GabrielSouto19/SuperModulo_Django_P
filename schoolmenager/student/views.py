from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from student.models import Student
import json 



@csrf_exempt
def list_students_view(request):
    students = Student.objects.all().values()
    students = json.dumps(students)
    return JsonResponse(students)
