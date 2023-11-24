from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse




def home_page(request):
    return render(request,"Home_page.html")


def view_my_student(request):
    return render(request,"view_my.html")


'''
def login_page(request):
    if request.method == "POST":
        data = request.POST
        id = data['student_id']
        password = data['student_password']
        students = StudentLogin.objects.all()
        stu = StudentLogin.objects.filter(login_id = id)
        if len(stu) == 0:
            return HttpResponse('Users not found')
        stu = stu.filter(login_password = password)
        if len(stu) == 0:
            return HttpResponse('Wrong Password')
        st = stu[0].student_details
        mark = Marks.objects.filter(student = stu[0])
        total_marks = st.calculate_total_marks()

    # Calculate rank based on total marks
        #rank = StudentDetails.objects.filter(student_id__in=StudentLogin.objects.all()).annotate(total=Sum('student_id__marks__marks')).order_by('-total').values_list('student_id', flat=True).index(stu[0].student_id) + 1
        queryset = StudentDetails.objects.filter(student_id__in=StudentLogin.objects.all()).annotate(total=Sum('student_id__marks__marks')).order_by('-total')

        rank = 0
        count = 1
        print(queryset)
        for quer in queryset:
            print(quer,stu[0])
            if quer == st:
                print('hey')
                rank = count
            count += 1
        
            
        context = {'stud': st, 'mark': mark, 'total_marks': total_marks, 'rank': rank,'q':queryset}
        return render(request,'view_my.html',context)
        
    

    return render(request,"login.html")


'''



from django.db.models import Sum


def view_student(request, id1, id2):
    st = StudentLogin.objects.filter(student_id=id1)
        
    l = st[0].student_details
    u = Unit.objects.filter(unit_id=id2)
    
    total_marks = 0
    rank = 1

    if st and u:
        # Retrieve marks for the specified unit
        marks = Marks.objects.filter(unit=u[0])
        st_mark = marks.filter(student=st[0])

        for m in  st_mark:
            total_marks += m.marks

        # Determine rank based on total marks, considering ties for the specified unit
        if total_marks > 0:
            higher_ranks = marks.filter(marks__gt=total_marks).count()
            rank += higher_ranks

    context = {'stud': l, 'mark': st_mark, 'total_marks': total_marks, 'rank': rank}

    return render(request, "view_my_new.html", context)




def stud_login(request):
    print('inside student_login')
    if request.method == "POST":
        data = request.POST
        id = data['login_id']
        password = data['student_password']

        stu = StudentLogin.objects.filter(login_id=id, login_password=password)
        units = Unit.objects.all()
        context = {'stud':stu[0], 'unit':units}
        return render(request, "student_portal.html", context)

    return render(request,'stud_login.html')


'''
def student_portal(request, id1):
    st = StudentLogin.objects.filter(student_id=id1)
    units = Unit.objects.all()
    stu = StudentDetails.objects.filter(student_id = st[0])
    print(stu[0].st_name)
    context = {'stud':stu[0], 'unit':units}
    return render(request, "student_portal.html", context)

'''


def logout_page(request):
    logout(request)
    return redirect('tlg/')

def Teacher_login_page(request):
    if request.method == "POST":
        data = request.POST
        Username = data['teacher_login_id']
        Password = data['Teacher_password']


        if not User.objects.filter(username = Username):
            messages.error(request,"Invalid Username")
            return redirect("/tlg")
        
        user = authenticate(username = Username,password = Password)
        if user is None:
            messages.error(request,"Incorrect password")
            return redirect("/Teacher_login_page")
        else:
            login(request,user)
            return redirect("/teacher/") 
    return render(request,"teacher_login.html")


@login_required(login_url="/tlg/")
def Teacher_view(request):
    return render(request, "Teacher_view_page.html")



def teacher_second_page(request,st_id):
    st = StudentLogin.objects.filter(student_id=st_id)
    units = Unit.objects.all()
    stu = StudentDetails.objects.filter(student_id = st[0])
    context = {'stud':stu[0], 'unit':units}
    return render(request,"teacher_second_page.html",context)

@login_required(login_url="/tlg/")
def view_students(request,standard):
    queryset = StudentLogin.objects.filter(student_details__st_standard = standard)
    context = {'students':queryset,'standard':standard}
    return render(request,"view_all_students.html",context)

import random


@login_required(login_url="/tlg/")
def new_exam(request):
    if request.method == "POST":
        data = request.POST
        exam_name = data['exam']
        un = Unit.objects.create(unit_name = exam_name)
        stu = StudentLogin.objects.all()
        sub = Subject.objects.all()
        for st in stu:
            for su in sub:
                Marks.objects.create(student = st,subject = su, unit = un, marks = random.randint(30,100))
    

    u = Unit.objects.all()
    context = {'unit': u}
    return render(request,"new_exam.html", context)
    


@login_required(login_url="/tlg/")
def update_exam(request,id1):
    queryset = Unit.objects.get(unit_id=id1)
    if request.method == "POST":
        data = request.POST

        unit_name = data['unit'] 
        queryset.unit_name = unit_name 
        
        
        queryset.save()
        return redirect('/new_exam')
    context = {'unit':queryset}
    return render(request,'update_exam.html',context)



def delete_exam(request,id1):
    return HttpResponse("<h1>You need adminstrator permission to do this</h1>")






@login_required(login_url="/tlg/")
def update_student(request,st_id,unit_id):
    stu = StudentLogin.objects.filter(student_id = st_id)
    st = stu[0].student_details
    unit = Unit.objects.filter(unit_id = unit_id)
    mark = Marks.objects.filter(student = stu[0],unit_id = unit[0] )
    if request.method == 'POST':
        data = request.POST
        tm = data['telugu']
        hm = data['hindi']
        em = data['english']
        mm = data['maths']
        pm = data['physics']
        sm = data['social']

        st_name = data['st_name']
        st_par_name = data['par_name']
        st_birth_year = data['birth_year']
        st_standard = data['standard']
        st_birth_place = data['birth_place']
        st.st_name = st_name
        st.st_birth_year = st_birth_year
        st.st_standard = st_standard
        st.st_parent_name = st_par_name
        st.st_birth_place = st_birth_place

        for m in mark:
            if m.subject.subject_name == 'Telugu':
                m.marks = tm
                m.save()
            if m.subject.subject_name == 'Hindi':
                m.marks = hm
                m.save()
            if m.subject.subject_name == 'English':
                m.marks = em
                m.save()
            if m.subject.subject_name == 'Maths':
                m.marks = mm
                m.save()
            if m.subject.subject_name == 'Physics':
                m.marks = pm
                m.save()
            if m.subject.subject_name == 'Social':
                m.marks = sm
                m.save()

        

        st.save()
        
        return redirect("/teacher")
        

    context = {'stud': st, 'mark': mark}
    return render(request,'update_student.html',context)




@login_required(login_url="/tlg/")
def add_student(request):
    if request.method == 'POST':
        data = request.POST
        st_name = data["st_name"]
        st_standard = data["standard"]
        st_birth_year = data["Birth_year"]
        st_birth_place = data["Birth_Place"]
        st_parent = data["Parent_name"]
        st = StudentLogin.objects.latest('login_id')
        login_id = st.login_id + 1
        student_id = 'STU' + str(login_id)
        login_password = str(login_id) + st_name[:4]
        st = StudentLogin.objects.create(student_id = student_id,login_id = login_id, login_password = login_password)
        stu = StudentDetails.objects.create(student_id = st,st_name = st_name,st_standard = st_standard, st_birth_year = st_birth_year,
                                            st_birth_place = st_birth_place, st_parent_name = st_parent)
        subs = Subject.objects.all()
        for s in subs:
            Marks.objects.create(student = st,subject = s, marks = 1)
        
        return redirect("/teacher")


    return render(request,'add_student.html')