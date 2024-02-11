from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp.models import *
from myapp.serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class MyNotification(APIView):
    def get(self, request, *args, **kwargs):
        staff=Staff.objects.get(admin=request.user.id)
        notification=Staff_Notification.objects.filter(staff_id=staff)
        notificationserializer=Staff_NotificationSerializer(notification,many=True)
        return Response(notificationserializer.data)
    def get(self, request,pk,*args, **kwargs):
        staff=Staff.objects.get(id=pk)
        notification=Staff_Notification.objects.filter(staff_id=staff)
        notificationserializer=Staff_NotificationSerializer(notification,many=True)
        return Response(notificationserializer.data)
    
    
class NotificationStatusChange(APIView):
    def post(self, request,pk):
        notification=Staff_Notification.objects.get(id=pk)
        notification.status=1
        notification.seen=1
        notification.save()
        return Response({"msg": "notification status change successfully"}, status=status.HTTP_201_CREATED)
    
  
class LeaveHistory(APIView):
    def get(self,request,pk=None):
        staff_leave=Staff_leave.objects.get(staff_id=pk)
        serializer=StaffLeaveSerializer(staff_leave)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
  
    
class LeaveFromStaff(APIView):
    def post(self,request,pk=None):
        staff=Staff.objects.get(id=pk)
        data=request.data
        message=data['message']
        
        leave=Staff_leave(staff_id=staff,message=message)
        leave.save()
        return Response({"msg": "successfully sent message to leave"}, status=status.HTTP_201_CREATED)
    
#update it    
class FeedbackCreate(APIView):
    def post(self,request,pk=None):
        staff=Staff.objects.get(admin=pk)
        feedback=request.data['feedback']
        feedback=Staff_Feedback(staff_id=staff,feedback=feedback,feedback_reply="")
        feedback.save()
        
        return Response({"msg": "successfully feedback created"}, status=status.HTTP_201_CREATED)
    
    
class FeedbackHistory(APIView):
    def get(self,request,pk=None):
        staff=Staff.objects.get(admin=pk)
        feedback_history=Staff_Feedback.objects.filter(staff_id=staff)
        serializer=StaffFeedbackSerializer(feedback_history,many=True)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class SubjectsAndSessionYear(APIView):
    def get(self, request,pk=None):
        staff=Staff.objects.get(id=pk)
        subjects=Subject.objects.filter(staff=staff)
        subjectserializer=SubjectSerializer(subjects,many=True)
        sessionyear=Session_Year.objects.all()
        sessionyearserializer=SessionyearSerializer(sessionyear,many=True)
        data={
            "subjects":subjectserializer.data,
            "sessionyear":sessionyearserializer.data
        }
        return Response(data, status=status.HTTP_201_CREATED)
    
    
        
    