from django.db import models

class Course(models.Model):
    COURSE_CHOICES = [
    ('matematica', 'Matemática'),
    ('portugues', 'Português'),
    ('historia', 'História'),
    ('geografia', 'Geografia'),
    ('ciencias', 'Ciências'),
    ('ingles', 'Inglês'),
    ('ed_fisica', 'Educação Física'),
    ('artes', 'Artes'),
    ('literatura', 'Literatura'),
    ('quimica', 'Química'),
    ('fisica', 'Física'),
    ('biologia', 'Biologia'),
]
    name = models.CharField(max_length=255,choices=COURSE_CHOICES)
    description = models.TextField()
    def __str__(self) -> str:
        return f'{self.name}'

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField()
    courses = models.ManyToManyField(Course,related_name='students')

    def __str__(self) -> str:
        return f'{self.first_name} - {self.lastname}'