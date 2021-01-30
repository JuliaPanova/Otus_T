from django.shortcuts import render, redirect
from .models import Student, Teacher, Lesson
from .forms import SignUpForm 
from django.contrib.auth import login, authenticate
from datetime import datetime


def index_view(request):
    return render(request, 'my_class_app/index.html')


def book_view(request):
    date_str = request.POST.get("date", "")
    date = datetime.strptime(date_str, "%m/%d/%Y")
    teacher_id = request.POST.get("teacher_id", "")
    teacher = Teacher.objects.get(id=teacher_id)
    student = Student.objects.get(user=request.user)

    Lesson(student=student, teacher=teacher, date_time=date).save()
    return render(request, 'my_class_app/thanks.html') 


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                print('signup_view authenticate user:', user)
                name = request.POST.get("name","")
                print('name:', name)
                phone = request.POST.get("phone", "")
                print('phone:', phone)
                student = Student(name=name, phone=phone, user=user)
                student.save()
                login(request, user)
                return redirect('student')
            else:
                render(request, 'my_class_app/signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'my_class_app/signup.html', {'form': form})


def student_view(request):
    student = Student.objects.get(user=request.user)
    teachers = Teacher.objects.all()
    lessons = Lesson.objects.filter(student=student)
    return render(request, 'my_class_app/student.html', {'student': student, 'teachers': teachers, 'lessons':lessons})

