from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type', 'profile_pic','password']
        
        
    def update(self, instance, validated_data):
        # Check if the password is included in the validated data
        password = validated_data.get('password')

        # If password is provided, set it for the user instance
        if password is not None and password.strip() != " ":
            instance.set_password(password)
            
        profile_pic = validated_data.get('profile_pic')
        
        if profile_pic:
            instance.profile_pic = profile_pic

        # Update other fields using the superclass's update method
        return super().update(instance, validated_data)
    
class SessionyearSerializer(serializers.ModelSerializer):
    class Meta:
        model=Session_Year
        fields=['id','session_start','session_end',]
        
    

    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['id','name','created_at','updated_at']
        
        
class StudentSerializer(serializers.ModelSerializer):
    admin = CustomUserSerializer()  
    course_id = CourseSerializer()  
    session_Year_id = SessionyearSerializer()
    class Meta:
        model = Student
        fields = '__all__' 

class StaffSerializer(serializers.ModelSerializer):
    admin = CustomUserSerializer()
    class Meta:
        model = Staff
        fields = ['admin','address', 'gender', 'created_at', 'updated_at']
        
        
class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields =['id','name', 'created_at', 'updated_at']
        
        
        
class Staff_NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff_Notification
        fields = ['id', 'staff_id', 'message','status', 'created_at','seen'] 
        
        
        
class StaffLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff_leave
        fields = '__all__'
        
        
class StaffFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff_Feedback
        fields ='__all__'
        depth=2
        
        
class Student_NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Notification
        fields = ['id', 'student_id', 'message','status', 'created_at','seen']
        
        
class StudentFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff_Feedback
        fields ='__all__'
        depth=2
        
        
class StudentLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_leave
        fields = '__all__'
        
        
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = ['subject_id', 'attendence_data', 'session_year_id', 'created_at', 'updated_at']
        
class AttendanceReportSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Attendence_Report
        fields = ['student_id', 'attendence_id', 'created_at', 'updated_at']