from django.db import models

# Create your models here.

from django.db import models

class StudentLogin(models.Model):
    student_id = models.CharField(max_length=100, unique=True)
    login_id = models.IntegerField(unique=True)
    login_password = models.CharField(max_length=100)

class StudentDetails(models.Model):
    student_id = models.OneToOneField(StudentLogin, related_name='student_details', on_delete=models.CASCADE)
    st_name = models.CharField(max_length=100)
    st_birth_year = models.IntegerField(default=2001)
    st_birth_place = models.CharField(max_length=100,default='Hyderabad')
    st_parent_name = models.CharField(max_length=100)
    st_standard = models.IntegerField(default=9)

    def calculate_total_marks(self,id):
        u = Unit.objects.filter(unit_id = id)
        marks = Marks.objects.filter(student=self.student_id,unit = u[0] )
        return sum([mark.marks for mark in marks])  

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True,unique=True)
    unit_name = models.CharField(max_length=100)


class Marks(models.Model):
    student = models.ForeignKey(StudentLogin, related_name='marks', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='marks', on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, related_name="marks",on_delete=models.CASCADE)
    marks = models.IntegerField(default=25)

