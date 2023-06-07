from django.shortcuts import render, get_object_or_404
from .decorators import *
from .forms import User_Form, Subject_Form
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *
from django.http import HttpResponseNotAllowed
import json

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'GET':
        form = User_Form()
        return render(request, 'authentication/register.html', {"form":form})
    elif request.method == 'POST':
        form = User_Form(request.POST)
        if form.is_valid():
            form.save()
            uloga = str(form.cleaned_data['uloga'])
            if uloga == 'student':
                student = Korisnik.objects.get(username=form.cleaned_data['username'])
                print(student)
                all_subjects = Predmet.objects.all()
                for subject in all_subjects:
                    status = Upis(student = student, predmet = subject, status = 'neupisan')
                    status.save()
            return redirect('login')
        else:
            return redirect('register')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
@administrator_required
def students_view(request):
    all_students = Korisnik.objects.filter(uloga__name='student')
    return render(request, 'students/students.html', {'students': all_students})

@login_required
@administrator_required
def student_edit_view(request, id):
    try:
        user = get_object_or_404(Korisnik, id=id)
        if user is None:
            raise Exception
        else:
            if request.method == "POST":
                user_form = User_Form(request.POST, instance=user)
                if user_form.is_valid():
                    user_form.save()
                    return redirect('students')
                else:
                    return redirect('students')
            else:
                user_form = User_Form(instance=user)
                return render(request, 'students/student_edit.html', { 'form': user_form })
    except Exception as e:
        print(request, f'An error has occured while trying to accesses the edit page.')
    return render(request, 'students/student_edit.html', {})

@login_required
@administrator_required
def student_information_view(request, id):
    try:
        user = get_object_or_404(Korisnik, id=id)
        if user is None:
            raise Exception
        else:
            return render(request, 'students/student_information.html', { 'student_information': user})
    except Exception as e:
        print(request, f'An error has occured while trying to accesses the inforamtion page.')

@login_required
@administrator_required
def student_all_subjects_view(request, id):
    student = Korisnik.objects.get(id=id)
    all_statuses = Upis.objects.filter(student=student)
    first_semester = []
    second_semester = []
    third_semester = []
    fourth_semester = []
    fifth_semester = []
    sixth_semester = []
    seventh_semester = []
    eight_semester = []
    if student.status == 'izv':
        for status in all_statuses:
            if status.predmet.sem_izv == 1:
                first_semester.append({
                    'name': status.predmet.name,
                    'kod': status.predmet.kod,
                    'ects': status.predmet.ects,
                    'status': status.status,
                    'status_id': status.id
                })
            elif status.predmet.sem_izv == 2:
                second_semester.append({
                    'name': status.predmet.name,
                    'kod': status.predmet.kod,
                    'ects': status.predmet.ects,
                    'status': status.status,
                    'status_id': status.id
                })
            elif status.predmet.sem_izv == 3:
                third_semester.append({
                    'name': status.predmet.name,
                    'kod': status.predmet.kod,
                    'ects': status.predmet.ects,
                    'status': status.status,
                    'status_id': status.id
                })
            elif status.predmet.sem_izv == 4:
                fourth_semester.append({
                    'name': status.predmet.name,
                    'kod': status.predmet.kod,
                    'ects': status.predmet.ects,
                    'status': status.status,
                    'status_id': status.id
                })
            elif status.predmet.sem_izv == 5:
                fifth_semester.append({
                    'name': status.predmet.name,
                    'kod': status.predmet.kod,
                    'ects': status.predmet.ects,
                    'status': status.status,
                    'status_id': status.id
                })
            elif status.predmet.sem_izv == 6:
                sixth_semester.append({
                    'name': status.predmet.name,
                    'kod': status.predmet.kod,
                    'ects': status.predmet.ects,
                    'status': status.status,
                    'status_id': status.id
                })
            elif status.predmet.sem_izv == 7:
                seventh_semester.append({
                    'name': status.predmet.name,
                    'kod': status.predmet.kod,
                    'ects': status.predmet.ects,
                    'status': status.status,
                    'status_id': status.id
                })
            elif status.predmet.sem_izv == 8:
                eight_semester.append({
                    'name': status.predmet.name,
                    'kod': status.predmet.kod,
                    'ects': status.predmet.ects,
                    'status': status.status,
                    'status_id': status.id
                })
    else:
        for status in all_statuses:
            if status.predmet.sem_red == 1:
                first_semester.append({
                    'name': status.predmet.name,
                    'kod': status.predmet.kod,
                    'ects': status.predmet.ects,
                    'status': status.status,
                    'status_id': status.id
                })
            elif status.predmet.sem_red == 2:
                second_semester.append({
                    'name': status.predmet.name,
                    'kod': status.predmet.kod,
                    'ects': status.predmet.ects,
                    'status': status.status,
                    'status_id': status.id
                })
            elif status.predmet.sem_red == 3:
                third_semester.append({
                    'name': status.predmet.name,
                    'kod': status.predmet.kod,
                    'ects': status.predmet.ects,
                    'status': status.status,
                    'status_id': status.id
                })
            elif status.predmet.sem_red == 4:
                fourth_semester.append({
                    'name': status.predmet.name,
                    'kod': status.predmet.kod,
                    'ects': status.predmet.ects,
                    'status': status.status,
                    'status_id': status.id
                })
            elif status.predmet.sem_red == 5:
                fifth_semester.append({
                    'name': status.predmet.name,
                    'kod': status.predmet.kod,
                    'ects': status.predmet.ects,
                    'status': status.status,
                    'status_id': status.id
                })
            elif status.predmet.sem_red == 6:
                sixth_semester.append({
                    'name': status.predmet.name,
                    'kod': status.predmet.kod,
                    'ects': status.predmet.ects,
                    'status': status.status,
                    'status_id': status.id
                })
            elif status.predmet.sem_red == 7:
                seventh_semester.append({
                    'name': status.predmet.name,
                    'kod': status.predmet.kod,
                    'ects': status.predmet.ects,
                    'status': status.status,
                    'status_id': status.id
                })
            elif status.predmet.sem_red == 8:
                eight_semester.append({
                    'name': status.predmet.name,
                    'kod': status.predmet.kod,
                    'ects': status.predmet.ects,
                    'status': status.status,
                    'status_id': status.id
                })
    return render(request, 'students/student_all_subjects.html', {
        'first_semester': first_semester,
        'second_semester': second_semester,
        'third_semester': third_semester,
        'fourth_semester': fourth_semester,
        'fifth_semester': fifth_semester,
        'sixth_semester': sixth_semester,
        'seventh_semester': seventh_semester,
        'eight_semester': eight_semester
    })

@login_required
@administrator_required
def student_add_view(request):
    if request.method == 'GET':
        form = User_Form()
        return render(request, 'students/student_add.html', {"form":form})
    elif request.method == 'POST':
        form = User_Form(request.POST)
        if form.is_valid():
            form.save()
            student = Korisnik.objects.get(username=str(form.cleaned_data['username']))
            all_subjects = Predmet.objects.all()
            for subject in all_subjects:
                status = Upis(student = student, predmet = subject, status = 'neupisan')
                status.save()
            return redirect('students')
        else:
            return redirect('students')

@login_required
@administrator_or_profesor_required
def subjects_view(request):
    if request.user.uloga.name == "administrator":
        all_subjects = Predmet.objects.all()
    else:
        all_subjects = Predmet.objects.filter(nositelj=request.user)
    return render(request, 'subjects/subjects.html', { 'data': all_subjects})

@login_required
@administrator_required
def subject_add_view(request):
    profesors = Korisnik.objects.filter(uloga__name='profesor')
    if request.method == 'GET':
        form = Subject_Form()
        return render(request, 'subjects/subject_add.html', {"form":form, 'profesors': profesors })
    elif request.method == 'POST':
        form = Subject_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subjects')
        else:
            return redirect('subjects')

@login_required
@administrator_or_profesor_required
def subject_inforamtion_view(request, id):
    try:
        subject = get_object_or_404(Predmet, id=id)
        if subject is None:
            raise Exception
        else:
            return render(request, 'subjects/subject_information.html', { 'subject': subject})
    except Exception as e:
        print(request, f'An error has occured while trying to accesses the inforamtion page.')

@login_required
@administrator_required
def subject_edit_view(request, id):
    try:
        subject = get_object_or_404(Predmet, id=id)
        profesors = Korisnik.objects.filter(uloga__name='profesor')
        if subject is None:
            raise Exception
        else:
            if request.method == "POST":
                subject_form = Subject_Form(request.POST, instance=subject)
                if subject_form.is_valid():
                    subject_form.save()
                    return redirect('subjects')
                else:
                    return redirect('subjects')
            else:
                subject_form = Subject_Form(instance=subject)
                return render(request, 'subjects/subject_edit.html', { 'form': subject_form, 'profesors': profesors})
    except Exception as e:
        print(request, f'An error has occured while trying to accesses the edit page.')
    return render(request, 'subjects/subject_edit.html', {})

@login_required
@administrator_or_profesor_required
def subject_all_students_view(request, subject_id):
    subject = Predmet.objects.get(id=subject_id)
    all_upisi = Upis.objects.filter(predmet=subject)
    all_enrolled_students = []
    all_failed_students = []
    all_passed_students = []
    for upis in all_upisi:
        if upis.status == 'upisan':
            all_enrolled_students.append({
                'firstName': upis.student.first_name,
                'lastName':  upis.student.last_name,
                'username': upis.student.username,
                'status_id': upis.id
            })
        elif upis.status == 'izgubljen_potpis':
            all_failed_students.append({
                'firstName': upis.student.first_name,
                'lastName':  upis.student.last_name,
                'username': upis.student.username,
                'status_id': upis.id
            })
        elif upis.status == 'polozen':
            all_passed_students.append({
                'firstName': upis.student.first_name,
                'lastName':  upis.student.last_name,
                'username': upis.student.username,
                'status_id': upis.id
            })
    return render(request, 'students/students_by_subject.html', {
        'enrolled_students': all_enrolled_students,
        'failed_students': all_failed_students,
        'passed_students': all_passed_students
    })

@login_required
@administrator_required
def profesors_view(request):
    all_profesors = Korisnik.objects.filter(uloga__name='profesor')
    return render(request, 'profesors/profesors.html', {'profesors': all_profesors })

@login_required
@administrator_required
def profesor_edit_view(request, id):
    try:
        profesor = get_object_or_404(Korisnik, id=id)
        if profesor is None:
            raise Exception
        else:
            if request.method == "POST":
                profesor_form = User_Form(request.POST, instance=profesor)
                print(profesor_form.errors)
                if profesor_form.is_valid():
                    profesor_form.save()
                    return redirect('profesors')
                else:
                    return redirect('profesors')
            else:
                profesor_form = User_Form(instance=profesor)
                return render(request, 'profesors/profesor_edit.html', { 'form': profesor_form })
    except Exception as e:
        print(request, f'An error has occured while trying to accesses the edit page.')
    return render(request, 'profesors/profesor_edit.html', {})

@login_required
@administrator_required
def profesor_information_view(request, id):
    try:
        profesor = get_object_or_404(Korisnik, id=id)
        if profesor is None:
            raise Exception
        else:
            return render(request, 'profesors/profesor_information.html', { 'profesor_information': profesor})
    except Exception as e:
        print(request, f'An error has occured while trying to accesses the inforamtion page.')

@login_required
@administrator_required
def profesor_add_view(request):
    if request.method == 'GET':
        form = User_Form()
        return render(request, 'profesors/profesor_add.html', {"form":form})
    elif request.method == 'POST':
        form = User_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesors')
        else:
            return redirect('profesors')

@login_required
@administrator_required
def deletion_confirmation_student(request, id):
    if request.method == "GET":
        return render(request, 'students/confirm_deletion_student.html', { "data": id })
    return HttpResponseNotAllowed()

@login_required
@administrator_required
def delete_student(request, id):
    student = Korisnik.objects.get(id=id)
    if 'yes' in request.POST:
        student.delete()
        return redirect('students')
    return redirect('students')

@login_required
@administrator_required
def deletion_confirmation_profesor(request, id):
    if request.method == "GET":
        return render(request, 'profesors/confirm_deletion_profesor.html', { "data": id })
    return HttpResponseNotAllowed()

@login_required
@administrator_required
def delete_profesor(request, id):
    profesor = Korisnik.objects.get(id=id)
    if 'yes' in request.POST:
        profesor.delete()
        return redirect('profesors')
    return redirect('profesors')

@login_required
@administrator_required
def deletion_confirmation_subject(request,id):
    if request.method == "GET":
        return render(request, 'subjects/confirm_deletion_subject.html', { "data": id })
    return HttpResponseNotAllowed()

@login_required
@administrator_required
def delete_subject(request, id):
    subject = Predmet.objects.get(id=id)
    if 'yes' in request.POST:
        subject.delete()
        return redirect('subjects')
    return redirect('subjects')

#dili sve po semestrima
@login_required
@student_required
def student_enrollment_form(request):
    if request.method == "GET":
        all_statuses = Upis.objects.filter(student=request.user)
        first_semester = []
        second_semester = []
        third_semester = []
        fourth_semester = []
        fifth_semester = []
        sixth_semester = []
        seventh_semester = []
        eight_semester = []
        if request.user.status == 'izv':
            for status in all_statuses:
                if status.predmet.sem_izv == 1:
                    first_semester.append({
                        'id': status.predmet.pk,
                        'name': status.predmet.name,
                        'kod': status.predmet.kod,
                        'ects': status.predmet.ects,
                        'status': status.status,
                        'status_id': status.id
                    })
                elif status.predmet.sem_izv == 2:
                    second_semester.append({
                        'id': status.predmet.pk,
                        'name': status.predmet.name,
                        'kod': status.predmet.kod,
                        'ects': status.predmet.ects,
                        'status': status.status,
                        'status_id': status.id
                    })
                elif status.predmet.sem_izv == 3:
                    third_semester.append({
                        'id': status.predmet.pk,
                        'name': status.predmet.name,
                        'kod': status.predmet.kod,
                        'ects': status.predmet.ects,
                        'status': status.status,
                        'status_id': status.id
                    })
                elif status.predmet.sem_izv == 4:
                    fourth_semester.append({
                        'id': status.predmet.pk,
                        'name': status.predmet.name,
                        'kod': status.predmet.kod,
                        'ects': status.predmet.ects,
                        'status': status.status,
                        'status_id': status.id
                    })
                elif status.predmet.sem_izv == 5:
                    fifth_semester.append({
                        'id': status.predmet.pk,
                        'name': status.predmet.name,
                        'kod': status.predmet.kod,
                        'ects': status.predmet.ects,
                        'status': status.status,
                        'status_id': status.id
                    })
                elif status.predmet.sem_izv == 6:
                    sixth_semester.append({
                        'id': status.predmet.pk,
                        'name': status.predmet.name,
                        'kod': status.predmet.kod,
                        'ects': status.predmet.ects,
                        'status': status.status,
                        'status_id': status.id
                    })
                elif status.predmet.sem_izv == 7:
                    seventh_semester.append({
                        'id': status.predmet.pk,
                        'name': status.predmet.name,
                        'kod': status.predmet.kod,
                        'ects': status.predmet.ects,
                        'status': status.status,
                        'status_id': status.id
                    })
                elif status.predmet.sem_izv == 8:
                    eight_semester.append({
                        'id': status.predmet.pk,
                        'name': status.predmet.name,
                        'kod': status.predmet.kod,
                        'ects': status.predmet.ects,
                        'status': status.status,
                        'status_id': status.id
                    })
        else:
            for status in all_statuses:
                if status.predmet.sem_red == 1:
                    first_semester.append({
                        'id': status.predmet.pk,
                        'name': status.predmet.name,
                        'kod': status.predmet.kod,
                        'ects': status.predmet.ects,
                        'status': status.status,
                        'status_id': status.id
                    })
                elif status.predmet.sem_red == 2:
                    second_semester.append({
                        'id': status.predmet.pk,
                        'name': status.predmet.name,
                        'kod': status.predmet.kod,
                        'ects': status.predmet.ects,
                        'status': status.status,
                        'status_id': status.id
                    })
                elif status.predmet.sem_red == 3:
                    third_semester.append({
                        'id': status.predmet.pk,
                        'name': status.predmet.name,
                        'kod': status.predmet.kod,
                        'ects': status.predmet.ects,
                        'status': status.status,
                        'status_id': status.id
                    })#<button type="submit" name="values" value='{ "subject" : {{ subject.id }}, "status": "upisan" }' class="btn btn-outline-primary mt-2">Enroll</button>
                elif status.predmet.sem_red == 4:
                    fourth_semester.append({
                        'id': status.predmet.pk,
                        'name': status.predmet.name,
                        'kod': status.predmet.kod,
                        'ects': status.predmet.ects,
                        'status': status.status,
                        'status_id': status.id
                    })
                elif status.predmet.sem_red == 5:
                    fifth_semester.append({
                        'id': status.predmet.pk,
                        'name': status.predmet.name,
                        'kod': status.predmet.kod,
                        'ects': status.predmet.ects,
                        'status': status.status,
                        'status_id': status.id
                    })
                elif status.predmet.sem_red == 6:
                    sixth_semester.append({
                        'id': status.predmet.pk,
                        'name': status.predmet.name,
                        'kod': status.predmet.kod,
                        'ects': status.predmet.ects,
                        'status': status.status,
                        'status_id': status.id
                    })
                elif status.predmet.sem_red == 7:
                    seventh_semester.append({
                        'id': status.predmet.pk,
                        'name': status.predmet.name,
                        'kod': status.predmet.kod,
                        'ects': status.predmet.ects,
                        'status': status.status,
                        'status_id': status.id
                    })
                elif status.predmet.sem_red == 8:
                    eight_semester.append({
                        'id': status.predmet.pk,
                        'name': status.predmet.name,
                        'kod': status.predmet.kod,
                        'ects': status.predmet.ects,
                        'status': status.status,
                        'status_id': status.id
                    })
        return render(request, 'students/enrollment_form.html', {
            'first_semester': first_semester,
            'second_semester': second_semester,
            'third_semester': third_semester,
            'fourth_semester': fourth_semester,
            'fifth_semester': fifth_semester,
            'sixth_semester': sixth_semester,
            'seventh_semester': seventh_semester,
            'eight_semester': eight_semester
        })
    elif request.method == "POST":
        print(request.POST.get('values'))
        values = json.loads(request.POST.get('values'))
        subject = Predmet.objects.get(id=values["subject"])
        status = Upis.objects.get(student=request.user, predmet=subject)
        status.status = values["status"]
        status.save()
        #it works now just implement the logic for enrolling
        return redirect('enrollment_form')
    else: 
        return HttpResponseNotAllowed()

#neka prosljeduje upis ne subject i student id
@login_required
@administrator_or_profesor_required
def subject_change_student_enrollment(request, status_id):
    if request.method == "GET":
        return render(request, 'students/change_student_status.html', { 'status_id': status_id })
    elif request.method == "POST":
        status = request.POST.get('status')
        upis = Upis.objects.get(id=request.POST.get('status_id'))
        upis.status = status
        upis.save()
        return redirect('home')

