from django.shortcuts import render
from .models import Student, Teacher

def index_view(request):
    return render(request, 'my_class_app/index.html')

def book_view(request):
    student_id = request.POST.get("student_id", "")
    return render(request, 'my_class_app/thanks.html', {'student_id':student_id})



def student_view(request):

    nologin = request.POST.get("nologin", "0")

    if nologin == "1":
        student_id = request.POST.get("student_id", "")
        student = Student.objects.get(id=student_id)
    elif request.POST.get("new_user", "1") == '1':
        name = request.POST.get("name","")
        phone = request.POST.get("phone","")
        login = request.POST.get("login","")
        psword = request.POST.get("pswrd","")
        student = Student(name=name, phone=phone, login=login, pswrd=psword)
        student.save()
    else:
        login = request.POST.get("login","")
        psword = request.POST.get("pswrd","")
        student = Student.objects.get(login=login, pswrd=psword)

    teachers = Teacher.objects.all()
    return render(request, 'my_class_app/student.html', {'student':student, 'teachers': teachers})
