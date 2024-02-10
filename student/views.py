from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp.models import *
from myapp.serializers import *
from rest_framework.response import Response
from rest_framework import status

class MyNotification(APIView):
    def get(self, request,pk=None):
        student=Student.objects.get(id=pk)
        notification=Student_Notification.objects.filter(student_id=student)
        serializer=Student_NotificationSerializer(notification,many=True)
        return Response(serializer.data)
    
class NotificationStatusChange(APIView):
    def post(self, request,pk):
        notification=Student_Notification.objects.get(id=pk)
        notification.status=1
        notification.seen=1
        notification.save()
        return Response({"msg": "notification status change successfully"}, status=status.HTTP_201_CREATED)
    
    
class StudentFeedbackCreate(APIView):
    def post(self,request,pk=None):
        student=Student.objects.get(admin=pk)
        feedback=request.data['feedback']
        feedback=Student_Feedback(student_id=student,feedback=feedback,feedback_reply="")
        feedback.save()
        
        return Response({"msg": "successfully feedback created"}, status=status.HTTP_201_CREATED)
    
    
class StudentFeedbackHistory(APIView):
    def get(self,request,pk=None):
        student=Student.objects.get(admin=pk)
        feedback_history=Student_Feedback.objects.filter(student_id=student)
        serializer=StudentFeedbackSerializer(feedback_history,many=True)
        return Response(serializer.data)
    
 
class LeaveFromStudent(APIView):
    def post(self,request,pk=None):
        student=Student.objects.get(id=pk)
        data=request.data
        message=data['message']
        
        leave=Student_leave(student_id=student,message=message)
        leave.save()
        return Response({"msg": "successfully sent message to leave"}, status=status.HTTP_201_CREATED) 
    
class LeaveHistory(APIView):
    def get(self,request,pk=None):
        student_leave=Student_leave.objects.get(student_id=pk)
        serializer=StudentLeaveSerializer(student_leave)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
  
    
