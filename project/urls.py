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
from EnrollmentApp.views import add_user, logout_view, success_login, add_subject, cover_view
from EnrollmentApp.views import lista_predmeta, promjena_predmeta, student_list, edit_student, professor_list, edit_professor
from EnrollmentApp.views import create_enrollment,enrollment_list, popis_studenata
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_user/', add_user, name='add_user'),
    path('success/', success_login, name='success'),
    # path('success/', success, name='success'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('add_subject/', add_subject, name='add_subject'),
    path('subjects/', lista_predmeta, name='lista_predmeta'),
    path('subjects/<int:predmet_id>/promjena/', promjena_predmeta, name='promjena_predmeta'),
    path('subjects/<int:predmet_id>/popis_studenata/', popis_studenata, name='popis_studenata'),
    path('students/', student_list, name='student_list'),
    path('students/<int:student_id>/edit/', edit_student, name='edit_student'),
    # path('enrollments/', enrollment_list, name='enrollment_list'),
    path('enrollments/create/', create_enrollment, name='create_enrollment'),
    # path('enrollments/<int:enrollment_id>/edit/', edit_enrollment, name='edit_enrollment'),
    path('student_list/', student_list, name='student_list'),
    path('edit_student/<int:student_id>/', edit_student, name='edit_student'),
    path('enrollment_list/<int:student_id>/', enrollment_list, name='enrollment_list'),
    path('professor_list/', professor_list, name='professor_list'),
    path('edit_professor/<int:professor_id>/', edit_professor, name='edit_professor'),
    path('cover/',cover_view, name='cover_view'),
    
]