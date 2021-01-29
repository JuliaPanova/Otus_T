from django.contrib import admin
from django.urls import path
from my_class_app.views import index_view, student_view, book_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('student/', student_view, name='student'),
    path('book/', book_view, name='book')

]
