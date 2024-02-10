from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp.models import *
from myapp.serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class getcourseslist(APIView):
    def get(self, request, format=None):
        
        course=Course.objects.all()
        serializer=CourseSerializer(course,many=True)

        return Response(serializer.data)
    
    
class getsession_year_list(APIView):
    def get(self, request, format=None):
        session_year=Session_Year.objects.all()
        serializers=SessionyearSerializer(session_year)
        
        return Response(serializers.data)
    
    


class AddStudent(APIView):
    def post(self, request, pk=None, format=None):
        # Extract data from the request
        data = request.data
        email = data.get('email')
        username = data.get('username')
        
        # Check if pk is provided for update operation
        if pk:
            #you should use that email and username read only from frontend
            try:
                student = Student.objects.get(id=pk)
            except Student.DoesNotExist:
                return Response({"msg": "Student with provided ID does not exist"}, status=status.HTTP_400_BAD_REQUEST)

            # Update existing student data
            user = student.admin
            user_serializer = CustomUserSerializer(user, data=data)
            if user_serializer.is_valid():
                user_serializer.save()
            else:
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Update student data
            student_data = {
                'address': data.get('address'),
                'gender': data.get('gender'),
                'course_id': data.get('course_id'),
                'session_Year_id': data.get('session_Year_id')
            }
            student_serializer = StudentSerializer(student, data=student_data)
            if student_serializer.is_valid():
                student_serializer.save()
                return Response({"msg": "Student updated successfully"}, status=status.HTTP_200_OK)
            else:
                return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # For creation operation
        else:
            if CustomUser.objects.filter(email=email).exists():
                return Response({"msg": "A student with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)
            if CustomUser.objects.filter(username=username).exists():
                return Response({"msg": "A student with this username already exists"}, status=status.HTTP_400_BAD_REQUEST)
            
            
            user_serializer = CustomUserSerializer(data=data)
            if user_serializer.is_valid():
                user = user_serializer.save(user_type=3)  # Assign user type as 3 for student
                user.set_password(data['password'])  # Set password
                user.save()

                # Extract additional student data
                student_data = {
                    'admin': user.id,
                    'address': data.get('address'),
                    'gender': data.get('gender'),
                    'course_id': data.get('course_id'),
                    'session_Year_id': data.get('session_Year_id')
                }

                # Serialize and save student data
                student_serializer = StudentSerializer(data=student_data)
                if student_serializer.is_valid():
                    student_serializer.save()
                    return Response({"msg": "Successfully added student"}, status=status.HTTP_201_CREATED)
                else:
                    # If student data is not valid, delete the user created
                    user.delete()
                    return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            

class StudentList(APIView):
    def get(self, request, format=None):
        # Retrieve all students from the database
        students = Student.objects.all()
        # Serialize the data
        serializer = StudentSerializer(students, many=True)
        # Return serialized data as response
        return Response(serializer.data)



class StudentDetail(APIView):

    def get(self, request, pk, format=None):
        # Retrieve a single student object
        student = Student.objects.get(id=pk)
        # Serialize the data
        serializer = StudentSerializer(student)
        course=Course.objects.all()
        courseserializer=CourseSerializer(course,many=True)
        sessionyear=Course.objects.all()
        sessionyearserializer=CourseSerializer(sessionyear,many=True)
        
        data={
            'student': serializer.data,
            'course':courseserializer.data,
            'sessionyear':sessionyearserializer.data,
            
            
        }
        
        # Return serialized data as response
        return Response(data)

    def delete(self, request, pk, format=None):
        try:
            # Retrieve the student object from the CustomUser model
            user = CustomUser.objects.get(id=pk, user_type=3)
        except CustomUser.DoesNotExist:
            return Response({"msg": "Student with provided ID does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the student object
        user.delete()
        return Response({"msg": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    
class Addcourse(APIView):
    def post(self,request,format=None):
        data=request.data
        course_name=data['name']
        course=Course(name=course_name)
        course.save()
        return Response({"msg": "Successfully course added"}, status=status.HTTP_201_CREATED)
 
 
        
class ViewCourse(APIView):
    def get(self,request,format=None):
        data=Course.objects.all()
        serializers=CourseSerializer(data,many=True)
        
        return Response({"courses": serializers.data}, status=status.HTTP_201_CREATED)
    
    
class EditCourse(APIView):
    def put(self, request, pk=None, format=None):
        course=Course.objects.get(id=pk)
        data=request.data
        serializers=CourseSerializer(data)
        new_course_name=data['name']
        course.name=new_course_name
        data={
            'course':serializers.data['name'],
            "course_id":pk
        }
        course.save()
        return Response({"data":data,"msg":"course updated successfully"}, status=status.HTTP_201_CREATED)
    
class DeleteCourse(APIView):
    def delete(self, request, pk, format=None):
        try:
            course = Course.objects.get(id=pk)
            course.delete()
            return Response({"msg": "Course deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
        
        
class AddStaff(APIView):
    def post(self, request, pk=None, format=None):
        # Extract data from the request
        data = request.data
        email = data.get('email')
        username = data.get('username')
        
        # Check if pk is provided for update operation
        if pk:
            #you should use that email and username read only from frontend
            try:
                staff = Staff.objects.get(id=pk)
            except Staff.DoesNotExist:
                return Response({"msg": "Staff with provided ID does not exist"}, status=status.HTTP_400_BAD_REQUEST)

            # Update existing student data
            user = staff.admin
            user_serializer = CustomUserSerializer(user, data=data)
            if user_serializer.is_valid():
                user_serializer.save()
            else:
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Update student data
            staff_data = {
                'address': data.get('address'),
                'gender': data.get('gender'),
                # 'course_id': data.get('course_id'),
                # 'session_Year_id': data.get('session_Year_id')
            }
            staff_serializer = StaffSerializer(staff, data=staff_data)
            if staff_serializer.is_valid():
                staff_serializer.save()
                return Response({"msg": "Staff updated successfully"}, status=status.HTTP_200_OK)
            else:
                return Response(staff_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # For creation operation
        else:
            if CustomUser.objects.filter(email=email).exists():
                return Response({"msg": "A staff with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)
            if CustomUser.objects.filter(username=username).exists():
                return Response({"msg": "A staff with this username already exists"}, status=status.HTTP_400_BAD_REQUEST)
            
            
            user_serializer = CustomUserSerializer(data=data)
            if user_serializer.is_valid():
                user = user_serializer.save(user_type=2)  # Assign user type as 2 for staff
                user.set_password(data['password'])  # Set password
                user.save()

                # Extract additional student data
                staff_data = {
                    'admin': user.id,
                    'address': data.get('address'),
                    'gender': data.get('gender'),
                    #'course_id': data.get('course_id'),
                    #'session_Year_id': data.get('session_Year_id')
                }

                # Serialize and save student data
                staff_serializer = StaffSerializer(data=staff_data)
                if staff_serializer.is_valid():
                    staff_serializer.save()
                    return Response({"msg": "Successfully added staff"}, status=status.HTTP_201_CREATED)
                else:
                    # If student data is not valid, delete the user created
                    user.delete()
                    return Response(staff_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class ViewStaff(APIView):
    def get(self, request, format=None):
        all_staff=Staff.objects.all()
        serializers=StaffSerializer(all_staff,many=True)
        return Response({"data":serializers.data }, status=status.HTTP_200_OK)
    
    
    
class StaffDetail(APIView):
    
    def get(self, request, pk, format=None):
        # Retrieve a single staff object
        staff = Staff.objects.get(id=pk)
        # Serialize the data
        serializer = StaffSerializer(staff)
        
        data={
            'student': serializer.data   
            }
        
        # Return serialized data as response
        return Response(data)

    def delete(self, request, pk, format=None):
        try:
            # Retrieve the staff object from the CustomUser model
            user = CustomUser.objects.get(id=pk, user_type=2)
        except CustomUser.DoesNotExist:
            return Response({"msg": "Student with provided ID does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the student object
        user.delete()
        return Response({"msg": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    
class SubjectAddandView(APIView):
    def get(self, request, *args, **kwargs):

        staffs=Staff.objects.all()
        courses=Course.objects.all()
        staff_serializer = StaffSerializer(staffs, many=True)
        course_serializer = CourseSerializer(courses, many=True)
        
        data = {
            'staffs': staff_serializer.data,
            'courses': course_serializer.data
        }
        
        return Response({"data": data}, status=status.HTTP_201_CREATED)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        
        subject_name = data.get('subject_name')  
        course_id = data.get('course_id')
        staff_id = data.get('staff_id')
        
        course=Course.objects.get(id=course_id)
        staff=Staff.objects.get(id=staff_id)
        
        subject=Subject(name=subject_name,course=course,staff=staff)
        subject.save()
        
        
        
        return Response({ "msg": "Successfully added subject"}, status=status.HTTP_201_CREATED)

    
        
# class SubjectAdd(APIView):
#     def post(self, request, *args, **kwargs):
#         # Step 1: Validate request data with serializer

#         subject_serializer = SubjectSerializer(data=request.data)
#         if not subject_serializer.is_valid():
#             return Response(subject_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         # Extract subject data from validated serializer
#         validated_data = subject_serializer.validated_data
#         subject_name = validated_data.get('name')
#         course_id = validated_data.get('course_id')
#         staff_id = validated_data.get('staff_id')
        
#         try:
#             # Step 2: Get Course and Staff instances
#             course = Course.objects.get(id=course_id)
#             staff = Staff.objects.get(id=staff_id)
#         except (Course.DoesNotExist, Staff.DoesNotExist):
#             return Response("Invalid course_id or staff_id", status=status.HTTP_400_BAD_REQUEST)
        
#         # Step 3: Create and save the subject
#         subject = Subject(name=subject_name, course=course, staff=staff)
#         subject.save()
        
#         # Step 4: Serialize staff and course data
#         staffs = Staff.objects.all()
#         courses = Course.objects.all()
#         staff_serializer = StaffSerializer(staffs, many=True)
#         course_serializer = CourseSerializer(courses, many=True)
        
#         # Return response with serialized data and success message
#         data = {
#             'staffs': staff_serializer.data,
#             'courses': course_serializer.data
#         }
#         return Response({"data": data, "msg": "Successfully added subject"}, status=status.HTTP_201_CREATED)

class SubjectUpdate(APIView):
    def post(self,request,pk=None,format=None):
        subject_obj=Subject.objects.get(id=pk)
        
        data=request.data
        subject_name = data.get('subject_name')  
        course_id = data.get('course_id')
        staff_id = data.get('staff_id')
        
        course=Course.objects.get(id=course_id)
        staff=Staff.objects.get(id=staff_id)
        
        subject_obj.name = subject_name
        subject_obj.course = course
        subject_obj.staff = staff
        subject_obj.save()
        return Response({ "msg": "Successfully subject updated"}, status=status.HTTP_201_CREATED)
    
    
class  SubjectDelete(APIView):
    def delete(self,request,pk=None):
        subject=Subject.objects.get(id=pk)
        subject.delete()
        return Response({ "msg": "Successfully subject deleted"}, status=status.HTTP_201_CREATED)
        
        
        
class AddSession(APIView):
    def post(self, request, *args, **kwargs):
        data=request.data
        session_start=data.get('session_start')
        session_end=data.get('session_end')
        session=Session_Year(session_start=session_start, session_end=session_end)
        session.save()
        return Response({ "msg": "Successfully session added"}, status=status.HTTP_201_CREATED)
         
class ViewAllSessionYear(APIView):
    def get(self, request, *args, **kwargs):
        session_year=Session_Year.objects.all()
        serializer=SessionyearSerializer(session_year,many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class UpdateDeleteSessionYear(APIView):   
    def put(self,request,pk=None):
        session_year_obj=Session_Year.objects.get(id=pk)
        data=request.data
        session_start=data.get('session_start')
        session_end=data.get('session_end')
        session_year_obj.session_start=session_start
        session_year_obj.session_end=session_end
        session_year_obj.save()
        
        
        return Response({ "msg": "Successfully session year updated"}, status=status.HTTP_201_CREATED)
    def delete(self,request,pk=None):
        session_year_obj=Session_Year.objects.get(id=pk)
        session_year_obj.delete()
        return Response({ "msg": "Successfully session year deleted"}, status=status.HTTP_201_CREATED)
        
        
class HomePageView(APIView):
    def get(self, request, *args, **kwargs):
        total_student=Student.objects.all().count()
        total_staff=Staff.objects.all().count()
        total_course=Course.objects.all().count()
        total_subject=Subject.objects.all().count()

        student_gender_male=Student.objects.filter(gender='Male').count() 
        student_gender_female=Student.objects.filter(gender='FeMale').count() 

        data={
           'total_students':total_student,
           'total_staff':total_staff,
           'total_course':total_course,
           'total_subject':total_subject,
           'total_male_student':student_gender_male,
           'total_female_student':student_gender_female
          }
        return Response(data, status=status.HTTP_201_CREATED)



class ViewStaff_with_Notification_status(APIView):
    def get(self, request, format=None):
        all_staff=Staff.objects.all()
        serializers=StaffSerializer(all_staff,many=True)
        
        notification=Staff_Notification.objects.all()
        statusserialiser=Staff_NotificationSerializer(notification,many=True)
        
        result={
            "staff":serializers.data,
            "notification":statusserialiser.data
            
        }
        return Response(result, status=status.HTTP_201_CREATED)

        

class Send_Staff_Notification(APIView):
    def post(self,request,pk=None):
        staff=Staff.objects.get(id=pk)
        message=request.data['message']
        
        notification=Staff_Notification(
            staff_id=staff,
            message=message
        )
        notification.save()
        return Response({ "msg": "Successfully notification send to the staff"}, status=status.HTTP_201_CREATED)
    
    
    
class StaffApplyToLeave(APIView):
    def get(self,request):
        staff_leave=Staff_leave.objects.all()
        staff_leave_serializer=StaffLeaveSerializer(staff_leave, many=True)  
        return Response(staff_leave_serializer.data)  
    
    
class StaffLeaveApprove(APIView):
    def post(self,request,pk=None):
        leave=Staff_leave.objects.get(id=pk)
        leave.status=1
        leave.save()
        return Response({ "msg": "staff leave approve Successfully"}, status=status.HTTP_201_CREATED)
    
class StaffLeaveDisApprove(APIView):
    def post(self,request,pk=None):
        leave=Staff_leave.objects.get(id=pk)
        leave.status=0
        leave.save()
        return Response({ "msg": "staff leave approve Successfully"}, status=status.HTTP_201_CREATED)
    
        
class StaffFeedback(APIView):
    def get(self,request):
        feedback=Staff_Feedback.objects.all()
        serializer=StaffFeedbackSerializer(feedback, many=True)  
        return Response(serializer.data)  
    
    
class StaffFeedbackReply(APIView):
    def post(self, request,pk):
        feedback=Staff_Feedback.objects.get(id=pk)
        data=request.data
        reply=data['feedback_reply']
        feedback.feedback_reply=reply
        feedback.save()
        return Response({ "msg": "feedback Successfully sent"}, status=status.HTTP_201_CREATED)
    
    
class All_Student(APIView):
    def get(self,request):
        studetns=Student.objects.all()
        serializer=StudentSerializer(studetns, many=True)  
        return Response(serializer.data)
    
class StudentNotification(APIView):
    def post(self,request,pk=None):
        student=Student.objects.get(id=pk)
        data=request.data
        message=data['message']
        notification=Student_Notification(student_id=student,message=message)
        notification.save()
        return Response({ "msg": "notification Successfully sent"}, status=status.HTTP_201_CREATED)
    
class Student_Notification_History(APIView):
    def get(self,request):
        notifications=Student_Notification.objects.all()
        serializer=Student_NotificationSerializer(notifications,many=True)
        return  Response(serializer.data)
    
    
class StudentFeedback(APIView):
    def get(self,request):
        feedback=Student_Feedback.objects.all().order_by("-id")
        serializer=StudentFeedbackSerializer(feedback, many=True)  
        return Response(serializer.data) 
    
    
class StudentFeedbackReply(APIView):
    def post(self, request,pk):
        feedback=Student_Feedback.objects.get(id=pk)
        data=request.data
        reply=data['feedback_reply']
        feedback.feedback_reply=reply
        feedback.save()
        return Response({ "msg": "feedback Successfully sent"}, status=status.HTTP_201_CREATED)
    
        
        
    
class StudentApplyToLeave(APIView):
    def get(self,request):
        student_leave=Student_leave.objects.all()
        student_leave_serializer=StudentLeaveSerializer(student_leave, many=True)  
        return Response(student_leave_serializer.data)  
    
    
class StudentLeaveApprove(APIView):
    def post(self,request,pk=None):
        leave=Student_leave.objects.get(id=pk)
        leave.status=1
        leave.save()
        return Response({ "msg": "student leave approve Successfully"}, status=status.HTTP_201_CREATED)
    
class StudentLeaveDisApprove(APIView):
    def post(self,request,pk=None):
        leave=Student_leave.objects.get(id=pk)
        leave.status=0
        leave.save()
        return Response({ "msg": "student leave disapprove Successfully"}, status=status.HTTP_201_CREATED)
    
    
    
