from django.contrib import admin
from django.urls import path
from my_class_app.views import index_view, student_view, book_view, signup_view, TeacherListView, TeacherDetailView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('student/', student_view, name='student'),
    path('book/', book_view, name='book'),
    path('signup/', signup_view),
    path('signin/', auth_views.LoginView.as_view(template_name='my_class_app/signin.html')),
    path('teachers/', TeacherListView.as_view()),
    path('teacher/<int:pk>/', TeacherDetailView.as_view())

]
