"""
URL configuration for project project.

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
from EnrollmentApp import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_user/', views.add_user, name='add_user'),
    path('success/', views.success_login, name='success'),
    # path('success/', success, name='success'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('subjects/', views.lista_predmeta, name='lista_predmeta'),
    path('subjects/<int:predmet_id>/promjena/', views.promjena_predmeta, name='promjena_predmeta'),
    path('subjects/<int:predmet_id>/popis_studenata/', views.popis_studenata, name='popis_studenata'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/edit/', views.edit_student, name='edit_student'),
    # path('enrollments/', enrollment_list, name='enrollment_list'),
    path('enrollments/create/', views.create_enrollment, name='create_enrollment'),
    # path('enrollments/<int:enrollment_id>/edit/', edit_enrollment, name='edit_enrollment'),
    path('student_list/', views.student_list, name='student_list'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('enrollment_list/<int:student_id>/', views.enrollment_list, name='enrollment_list'),
    path('professor_list/', views.professor_list, name='professor_list'),
    path('edit_professor/<int:professor_id>/', views.edit_professor, name='edit_professor'),
    path('cover/',views.cover_view, name='cover_view'),
    path('professor/subjects/', views.professor_subjects, name='professor_subjects'),
    path('subject/student_list/<int:subject_id>/', views.subject_student_list, name='subject_student_list'),
    path('subject/edit_status/<int:subject_id>/<int:student_id>/', views.edit_status, name='edit_status'),
    path('subject/remove_subject_student/<int:subject_id>/<int:student_id>/', views.remove_subject_student, name='remove_subject_student'),
    path('forbidden/', views.forbidden, name='forbidden'),
    path('subject/passed_students/<int:subject_id>/', views.subject_passed_students, name='subject_passed_students'),
    path('subject/enrolled_students/<int:subject_id>/', views.subject_enrolled_students, name='subject_enrolled_students'),
    path('subject/failed_students/<int:subject_id>/', views.subject_failed_students, name='subject_failed_students'),
    path('subject/details/<int:subject_id>/', views.subject_details, name='subject_details'),
    path('upisni_list/', views.upisni_list, name='upisni_list'),
    path('enrolled_student/', views.enrolled_student, name='enrolled_student'),
    path('subject/remove_subject_students/<int:subject_id>/', views.remove_subject_students, name='remove_subject_student'),
    path('unenrolled_subjects/', views.unenrolled_subjects, name='unenrolled_subjects'),
    path('enroll_subject/<int:subject_id>/', views.enroll_subject, name='enroll_subject'),
    path('contact/', views.professor_list_new, name='contact'),
    path('remove_subjects_students/<int:subject_id>/', views.remove_subjects_students, name='remove_subjects_students'),
    path('users/', views.user_list, name='user_list'),
    path('remove_user/', views.remove_user, name='remove_user'),

]  
