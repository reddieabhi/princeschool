"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myschool.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("new_exam/",new_exam, name = 'new_exam'),
    path('tlg/',Teacher_login_page,name = "Teacher_login_page"),
    path("view_students/<standard>/",view_students,name = 'view_students'),
    path('teacher/', Teacher_view, name='Teacher'),
    path('teacher_second/<st_id>/',teacher_second_page,name = 'teacher_second_page'),
    #path('logout/',logout_page,name = 'logout_page'),
    path('teacher/logout/', logout_page, name='logout_page'),
    path('teacher/logout/tlg/',Teacher_login_page,name = "Teacher_login_page"),
    path('update_student/<st_id>/<unit_id>/',update_student,name = 'update_student'),
    path("add_stud/",add_student,name = 'add_student'),
    path("my_marks/<id1>/<id2>/",view_student, name = 'view_student'),
    path("stud_login/",stud_login,name = 'stud_login'),
    path("update_exam/<id1>/",update_exam,name = 'update_exam'),
    path("delete_exam/<id1>/",delete_exam, name = 'delete_exam'),
    #path("stud_portal/<id1>/",student_portal , name='student_portal'),
    path("",home_page,name="home_page")

]
