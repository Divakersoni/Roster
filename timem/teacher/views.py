from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from teacher.models import Department, Teacher,Subject
from .forms import DepartmentForm, SubjectForm, TeacherForm, SecForm, SemForm, ClassRoomForm, LabForm
from django.template import RequestContext
from timet.models import Teacher_final,Master_final,Lab_final,Room_final
from location.models import ClassRoom, Lab
from semclass.models import Sem,Sec
from location.lab_filter import search,check,search1
from location.room_filter import search2

###Front Page of site
def home(request):
    dpt = Department.objects.all()
    sem = Sem.objects.all()
    sec = Sec.objects.all()
    teacher=Teacher.objects.all()
    return render(request, 'index.html',{'dpt':dpt,'sem':sem,'sec':sec,'tec':teacher})

def master_tt(request, id):
    sec=Sec.objects.get(id=id)
    mf=Master_final.objects.filter(sec=sec)
    return render(request, 'tt_table.html',{'tf':mf})
#
# def teacher_tt(request,string):
#     tf = Teacher_final.objects.filter(teacher_name__teacher_initials=string)
#     return render(request,'tt_table.html',{'tf':tf})


def about(request):
    return render(request, 'about.html')


def generate(request):
    return render(request, 'generate.html')


###ctti functions


def ctti(request):
    return render(request, 'ctti.html')

def add_resources(request):
    return render(request, 'add_resources.html')

def update_resources(request):
    return render(request, 'update_resources.html')

def register_dept(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/click_here/')
    else:
        form = DepartmentForm()

    return render(request, 'register.html', {'form': form})


def register_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/click_here/')
    else:
        form = SubjectForm()

    return render(request, 'register.html', {'form': form})

def click_here(request):
    return render(request, 'click_here.html')

def register_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/click_here/')
    else:
        form = TeacherForm()

    return render(request, 'register.html', {'form': form})


def register_sec(request):
    if request.method == 'POST':
        form = SecForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/click_here/')
    else:
        form = SecForm()

    return render(request, 'register.html', {'form': form})


def register_sem(request):
    if request.method == 'POST':
        form = SemForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/click_here/')
    else:
        form = SemForm()

    return render(request, 'register.html', {'form': form})


def register_class(request):
    if request.method == 'POST':
        form = ClassRoomForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/click_here/')
    else:
        form = ClassRoomForm()

    return render(request, 'register.html', {'form': form})


def register_lab(request):
    if request.method == 'POST':
        form = LabForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/click_here/')
    else:
        form = LabForm()

    return render(request, 'register.html', {'form': form})

## dti login
def dti(request):
    dept=Department.objects.all()
    return render(request, 'dti_dept.html',{'dept':dept,'get':request.POST})

def dti_dept(request,id):
    return render(request, 'dti.html',{'id':id})

def view_resources(request,id):
    teachers=list()
    dept = Department.objects.get(id=id)
    t= Teacher.objects.all()
    for i in t:
        if i.subject1.department == dept:
            teachers.append(i)
        elif i.subject2.department == dept:
            teachers.append(i)
        elif i.subject3.department == dept:
            teachers.append(i)
        elif i.subject4.department == dept:
            teachers.append(i)
        else:
            pass
    return render(request, 'view_resource.html',{'teacher':teachers})

### View time Table
def view_time(request):
    return render(request, 'view_time.html')




##### Main code that will do the execution part
def timet1(request):
    l = Lab.objects.all()
    for i in l:
        lf = Lab_final.objects.filter(lab_no=i)
        if lf.__len__() == 0:
            for j in range(0, 6):
                l = Lab_final(lab_no=i, day_type=j + 1)
                l.save()
    c = ClassRoom.objects.all()
    for i in c:
        lf = Room_final.objects.filter(Room_no=i)
        if lf.__len__() == 0:
            for j in range(0, 6):
                l = Room_final(Room_no=i, day_type=j + 1)
                l.save()
    t = Teacher.objects.all()
    for i in t:
        lf = Teacher_final.objects.filter(teacher_name=i)
        if lf.__len__() == 0:
            for j in range(0, 6):
                l = Teacher_final(teacher_name=i, day_type=j + 1)
                l.save()
    m = Sec.objects.all().order_by('Section', 'sem')
    for i in m:
        lf = Master_final.objects.filter(sec=i)
        if lf.__len__() == 0:
            for j in range(0, 6):
                l = Master_final(sec=i, day_type=j + 1)
                l.save()
    dept = Department.objects.all()
    li = list()
    s = ''
    for x in dept:
        sem = Sem.objects.filter(department=x)
        for i in sem:
            a = list()
            b = list()
            s = str(i.sem) + str(x.department_initials)
            sub = Subject.objects.filter(department=x).filter(semester=i.sem).filter(type_subject=1).order_by('-teaching_hours_a_day')
            tec=list()
            t = Teacher.objects.all()
            for j in t:
                if j.subject1.department == x:
                    tec.append(j)
                elif j.subject2.department == x:
                    tec.append(j)
                elif j.subject3.department == x:
                    tec.append(j)
                elif j.subject4.department == x:
                    tec.append(j)
                else:
                    pass
            for j in tec:
                for k in sub:
                    if j.subject1 == k and j.teaching_hours_a_day_subject1 > 0:
                        if check(j, j.subject1, j.subject1.teaching_hours_a_day):
                            if j.subject1.teaching_hours_a_day == 3:
                                a.append([j, j.subject1, 1])
                            else:
                                b.append([j, j.subject1, 1])
                        else:
                            pass
                    elif j.subject2 == k and j.teaching_hours_a_day_subject3 > 0:
                        if check(j, j.subject2, j.subject2.teaching_hours_a_day):
                            if j.subject2.teaching_hours_a_day == 3:
                                a.append([j, j.subject2, 2])
                            else:
                                b.append([j, j.subject2, 2])
                        else:
                            pass
                    elif j.subject3 == k and j.teaching_hours_a_day_subject3 > 0:
                        if check(j, j.subject3, j.subject3.teaching_hours_a_day):
                            if j.subject3.teaching_hours_a_day == 3:
                                a.append([j, j.subject3, 3])
                            else:
                                b.append([j, j.subject3, 3])
                        else:
                            pass
                    elif j.subject4 == k and j.teaching_hours_a_day_subject4 > 0:
                        if check(j, j.subject4, j.subject4.teaching_hours_a_day):
                            if j.subject1.teaching_hours_a_day == 3:
                                a.append([j, j.subject4, 4])
                            else:
                                b.append([j, j.subject4, 4])
                        else:
                            pass
                    else:
                        pass
            sec = Sec.objects.filter(sem=i).order_by('Section')
            for j in sec:
                d = search(a, j, sub)
                e = search1(b, j, sub)

    s = ''
    for x in dept:
        sem = Sem.objects.filter(department=x)
        for i in sem:
            c = list()
            s = str(i.sem) + str(i.department.department_initials)
            sub = Subject.objects.filter(department=x).filter(semester=i.sem).filter(type_subject=0).order_by('-teaching_hours_a_day')
            tec = list()
            t = Teacher.objects.all()
            for j in t:
                if j.subject1.department == x:
                    tec.append(j)
                elif j.subject2.department == x:
                    tec.append(j)
                elif j.subject3.department == x:
                    tec.append(j)
                elif j.subject4.department == x:
                    tec.append(j)
                else:
                    pass
            for j in tec:
                for k in sub:
                    if j.subject1 == k and j.teaching_hours_a_day_subject1 > 0:
                        if check(j, j.subject1, j.subject1.teaching_hours_a_day):
                            c.append([j, j.subject1, 1])
                        else:
                            pass
                    elif j.subject2 == k and j.teaching_hours_a_day_subject2 > 0:
                        if check(j, j.subject2, j.subject2.teaching_hours_a_day):
                            c.append([j, j.subject2, 2])
                        else:
                            pass
                    elif j.subject3 == k and j.teaching_hours_a_day_subject3 > 0:
                        if check(j, j.subject3, j.subject3.teaching_hours_a_day):
                            c.append([j, j.subject3, 3])
                        else:
                            pass
                    elif j.subject4 == k and j.teaching_hours_a_day_subject4 > 0:
                        if check(j, j.subject4, j.subject4.teaching_hours_a_day):
                            c.append([j, j.subject4, 4])
                        else:
                            pass
                    else:
                        pass
            sec = Sec.objects.filter(sem=i).order_by('Section')
            for j in sec:
                d = search2(c, j, x)
                li.append(d)

    return render(request, 'index.html')
