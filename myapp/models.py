from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_CHOICES = (
        (1, 'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT'),
    )
    user_type = models.IntegerField(choices=USER_CHOICES, default=3)
    profile_pic = models.ImageField(upload_to='profile_pics', verbose_name='Profile Picture')
    
class Course(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class Session_Year(models.Model):
    session_start=models.CharField(max_length=100)
    session_end=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.session_start +" - "+self.session_end
    
    
class Student(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    gender=models.CharField(max_length=100)
    course_id=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    session_Year_id=models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.admin.first_name +" "+self.admin.last_name
    

    
class Staff(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    gender=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.admin.username
    
    
class Subject(models.Model):
    name=models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    staff=models.ForeignKey(Staff,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name   
    
    
    
class Staff_Notification(models.Model):
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    message=models.TextField()
    status=models.BooleanField(default=False)
    seen=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.staff_id.admin.first_name
    
    
class Staff_leave(models.Model):
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    data=models.CharField(max_length=100)
    message=models.TextField()
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.staff_id.admin.first_name+"-"+self.staff_id.admin.last_name
    
    
class Staff_Feedback(models.Model):
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.staff_id.admin.first_name+" "+self.staff_id.admin.last_name
    
    
class Student_Notification(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    message=models.TextField()
    status=models.BooleanField(default=False)
    seen=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.student_id.admin.first_name
    
    
class Student_Feedback(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.student_id.admin.first_name+" "+self.student_id.admin.last_name
    
    
class Student_leave(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    data=models.CharField(max_length=100)
    message=models.TextField()
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.student_id.admin.first_name+"-"+self.student_id.admin.last_name
    
    
class Attendence(models.Model):
    subject_id=models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    attendence_data=models.DateField()
    session_year_id=models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject_id
    
    
class Attendence_Report(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendence_id=models.ForeignKey(Attendence,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.student_id.admin.first_name+" "+self.student_id.admin.last_name
    