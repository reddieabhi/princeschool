from .models import *


import random

def create_marks():
    stu = StudentLogin.objects.all()
    subs = Subject.objects.all()
    
    for s in stu:
        for sub in subs:
            m = random.randint(1,100)
            Marks.objects.create(student = s,subject = sub, marks = m)


