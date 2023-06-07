"""
URL configuration for iwa_seminar project.

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
from student_managment_system import views
from django.contrib.auth.views import LoginView
from student_managment_system.views import logout_view
from student_managment_system.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('students/', students_view, name="students"),
    path('students/student_add', student_add_view, name="student_add"),
    path('students/student_edit/<int:id>', student_edit_view, name='student_edit'),
    path('students/student_information/<int:id>', student_information_view, name='student_information'),
    path('students/student_delete_confirmation/<int:id>', deletion_confirmation_student, name="student_delete_confirmation"),
    path('students/student_delete/<int:id>', delete_student, name="student_delete"),
    path('students/student_all_enrolled_subjects/<int:id>', student_all_subjects_view, name="student_all_enrolled_subjects"),
    path('subjects/', subjects_view, name="subjects"),
    path('subjects/subject_add', subject_add_view, name="subject_add"),
    path('students/subject_delete_confirmation/<int:id>', deletion_confirmation_subject, name="subject_delete_confirmation"),
    path('students/subject_delete/<int:id>', delete_subject, name="subject_delete"),
    path('subjects/subject_edit/<int:id>', subject_edit_view, name="subject_edit"),
    path('subjects/subject_information/<int:id>', subject_inforamtion_view, name="subject_information"),
    path('subjects/subject_all_students/<int:subject_id>', subject_all_students_view, name="subject_all_students"),
    path('change_student_status/<int:status_id>/', subject_change_student_enrollment, name='change_student_status'),    path('profesors/', profesors_view, name="profesors"),
    path('profesors/profesor_add', profesor_add_view, name="profesor_add"),
    path('profesors/profesor_edit/<int:id>', profesor_edit_view, name='profesor_edit'),
    path('profesors/profesor_information/<int:id>', profesor_information_view, name='profesor_information'),
    path('profesors/profesor_delete_confirmation/<int:id>', deletion_confirmation_profesor, name="profesor_delete_confirmation"),
    path('profesors/profesor_delete/<int:id>', delete_profesor, name="profesor_delete"),
    path('enrollment_form', student_enrollment_form, name="enrollment_form"),

]
