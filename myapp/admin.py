from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display=['id','username','user_type']
    
admin.site.register(CustomUser, CustomUserAdmin)

    
class CourseAdmin(admin.ModelAdmin):
    model=Course
    list_display=['id','name']


admin.site.register(Course,CourseAdmin)
class AdminSessionYear(admin.ModelAdmin):
    list_display = ('id','session_start','session_end')

admin.site.register(Session_Year,AdminSessionYear)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','admin', 'address', 'gender', 'course_id', 'session_Year_id', 'created_at', 'updated_at')

admin.site.register(Student, StudentAdmin)




class StaffAdmin(admin.ModelAdmin):
    list_display = ['id','admin', 'address', 'gender', 'created_at', 'updated_at']
    
    
admin.site.register(Staff)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course', 'staff', 'created_at', 'updated_at')

admin.site.register(Subject, SubjectAdmin)


class Staff_NotificationAdmin(admin.ModelAdmin):
    list_display = ('id','staff_id', 'message', 'created_at','status','seen')  

admin.site.register(Staff_Notification, Staff_NotificationAdmin)


@admin.register(Staff_leave)
class StaffLeaveAdmin(admin.ModelAdmin):
    list_display = ('id','staff_id', 'data', 'message', 'status', 'created_at', 'updated_at')
    
    
@admin.register(Staff_Feedback)
class StaffFeedbackAdmin(admin.ModelAdmin):
    list_display = ['id','staff_id', 'feedback', 'feedback_reply', 'created_at', 'updated_at']
    
    
class Student_NotificationAdmin(admin.ModelAdmin):
    list_display = ('id','student_id', 'message', 'created_at','status','seen')  

admin.site.register(Student_Notification, Student_NotificationAdmin)


@admin.register(Student_Feedback)
class StudentFeedbackAdmin(admin.ModelAdmin):
    list_display = ['id','student_id', 'feedback', 'feedback_reply', 'created_at', 'updated_at']
    
    
class StudentLeaveAdmin(admin.ModelAdmin):
    list_display = ('id','student_id','message','data', 'status', 'created_at', 'updated_at')


admin.site.register(Student_leave, StudentLeaveAdmin)


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id','subject_id', 'attendence_data', 'session_year_id', 'created_at', 'updated_at']

admin.site.register(Attendence, AttendanceAdmin)


class AttendanceReportAdmin(admin.ModelAdmin):
    list_display = ['id','student_id', 'attendence_id', 'created_at', 'updated_at']


admin.site.register(Attendence_Report, AttendanceReportAdmin)