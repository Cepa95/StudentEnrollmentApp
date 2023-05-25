from django.shortcuts import render, redirect, get_object_or_404
from .models import Korisnici, Predmeti, StudentEnrollment
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.urls import reverse
from .forms import PredmetForm, KorisniciForm, StudentEnrollmentForm, StudentEnrollmentForm1
from django.forms import modelformset_factory
from django.forms import formset_factory
from django.middleware.csrf import rotate_token
# Create your views here.




def check_admin(user):
    return user.role == 'administrator'


@login_required
@user_passes_test(check_admin)
def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        role = request.POST['role']
        status = request.POST['status']

        if password != repeat_password:
            error_message = "Passwords do not match."
            return render(request, 'add_user.html', {'error_message': error_message})

        user = Korisnici.objects.create_user(username=username, password=password,
                                             first_name=first_name, last_name=last_name,
                                             email=email, role=role, status=status)
        # Additional processing or redirect to a success page
        return redirect('/success/')

    return render(request, 'add_user.html')



@login_required
def success_login(request):
    user = request.user
    if user.role == 'administrator':
        return render(request, 'success.html', {'user': user})
    elif user.role == 'student':
        return render(request, 'success_student.html', {'user': user})
    else:
        return render(request, 'success.html', {'user': user})   



# @login_required
# def logout_view(request):
#         logout(request)
#         return redirect('/accounts/login/')


@login_required
def logout_view(request):
    logout(request)
    # Delete CSRF token (optional)
    rotate_token(request)
    return redirect('/accounts/login/')
    

@login_required
@user_passes_test(check_admin)
def add_subject(request):
    if request.method == 'POST':
        form = PredmetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success/') 
    else:
        form = PredmetForm()
    
    context = {
        'form': form,
        'professors': Korisnici.objects.filter(role='profesor')
    }
    return render(request, 'add_subject.html', context)


@login_required
@user_passes_test(check_admin)
def lista_predmeta(request):
    predmeti = Predmeti.objects.all()
    return render(request, 'lista_predmeta.html', {'predmeti': predmeti})


@login_required
@user_passes_test(check_admin)
def promjena_predmeta(request, predmet_id):
    predmet = get_object_or_404(Predmeti, id=predmet_id)
    form = PredmetForm(request.POST or None, instance=predmet)
    if form.is_valid():
        form.save()
        return redirect('lista_predmeta')
    return render(request, 'promjena_predmeta.html', {'form': form})


@login_required
@user_passes_test(check_admin)
def student_list(request):
    students = Korisnici.get_students()
    return render(request, 'student_list.html', {'students': students})


@login_required
@user_passes_test(check_admin)
def edit_student(request, student_id):
    student = get_object_or_404(Korisnici, id=student_id)
    form = KorisniciForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'edit_student.html', {'form': form})



# @login_required
# @user_passes_test(check_admin)
# def enrollment_list(request, student_id):
#     student = get_object_or_404(Korisnici, id=student_id)
#     EnrollmentFormSet = formset_factory(StudentEnrollmentForm, extra=0)
#     if request.method == 'POST':
#         formset = EnrollmentFormSet(request.POST)
#         if formset.is_valid():
#             for form in formset:
#                 enrollment = form.save(commit=False)
#                 enrollment.student = student
#                 enrollment.save()
#             return redirect('success')
#     else:
#         enrollments = StudentEnrollment.objects.filter(student=student)
#         initial_data = [{'subject': enrollment.subject, 'status': enrollment.status} for enrollment in enrollments]
#         formset = EnrollmentFormSet(initial=initial_data)
#     return render(request, 'enrollment_list.html', {'student': student, 'formset': formset})


@login_required
@user_passes_test(check_admin)
def enrollment_list(request, student_id):
    student = get_object_or_404(Korisnici, id=student_id)
    EnrollmentFormSet = formset_factory(StudentEnrollmentForm, extra=0)
    
    if request.method == 'POST':
        formset = EnrollmentFormSet(request.POST)
        
        if formset.is_valid():
            StudentEnrollment.objects.filter(student=student).delete()  # Delete existing enrollments for the student
            
            for form in formset:
                enrollment = form.save(commit=False)
                enrollment.student = student
                enrollment.save()
            
            return redirect('success')
    else:
        enrollments = StudentEnrollment.objects.filter(student=student)
        initial_data = [{'subject': enrollment.subject, 'status': enrollment.status} for enrollment in enrollments]
        formset = EnrollmentFormSet(initial=initial_data)
    
    context = {
        'student': student,
        'formset': formset
    }
    return render(request, 'enrollment_list.html', context)







@login_required
@user_passes_test(check_admin)
def create_enrollment(request):
    if request.method == 'POST':
        form = StudentEnrollmentForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentEnrollmentForm1()

    students = Korisnici.objects.filter(role='student')
    context = {
        'form': form,
        'students': students
    }
    return render(request, 'create_enrollment.html', context)


# @login_required
# @user_passes_test(check_admin)
# def edit_enrollment(request, pk):
#     enrollment = get_object_or_404(StudentEnrollment, pk=pk)
#     if request.method == 'POST':
#         form = StudentEnrollmentForm(request.POST, instance=enrollment)
#         if form.is_valid():
#             form.save()
#             return redirect('enrollment_list')
#     else:
#         form = StudentEnrollmentForm(instance=enrollment)
#     return render(request, 'edit_enrollment.html', {'form': form})


@login_required
@user_passes_test(check_admin)
def professor_list(request):
    professors = Korisnici.get_professors()
    return render(request, 'professor_list.html', {'professors': professors})



@login_required
@user_passes_test(check_admin)
def edit_professor(request, professor_id):
    professor = get_object_or_404(Korisnici, id=professor_id)
    form = KorisniciForm(request.POST or None, instance=professor)
    if form.is_valid():
        form.save()
        return redirect('profesor_list')
    return render(request, 'edit_professor.html', {'form': form})


def cover_view(request):
    return render(request, 'cover.html')
