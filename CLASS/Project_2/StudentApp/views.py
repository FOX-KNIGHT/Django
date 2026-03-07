from django.shortcuts import render
from .models import Student

# Create your views here.
def student_list(request):
    s = Student.objects.all()
    return render(request, 'StudentApp/Student_list.html',{'student':s})