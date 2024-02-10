from django.urls import path
from hod.views import *
urlpatterns = [
    path('home/', HomePageView.as_view(), name='hod_home_page'),
    #HOD home page
    
    
    
    
    
    
    path("getcourseslist/",getcourseslist.as_view(),name="courseslist"),
    path("getsession_year_list/",getsession_year_list.as_view(),name="getsession_year_list"),
    path("add_student/",AddStudent.as_view(),name="getsession_year_list"),
    path("get_all_student/",StudentList.as_view(),name="get_student_list"),
    #hod are able to see,edit or update,and delete specific student here
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
    path('students/delete/<int:pk>/', StudentDetail.as_view(), name='student_detail_delete'),
    path("update_student/<int:pk>/",AddStudent.as_view(),name="update_student_here"),
    
    #
    path("add_course/",Addcourse.as_view(),name="add_course"),
    path("view_course/",ViewCourse.as_view(),name="view_course"),
    path("course_edit/<int:pk>/",EditCourse.as_view(),name="edit_course"),
    path("course_delete/<int:pk>/",DeleteCourse.as_view(),name="delete_course"),
    
    #
    path("add_staff/",AddStaff.as_view(),name="add_staff"),
    #use put method
    path("update_staff/<int:pk>/",AddStaff.as_view(),name="update_staff"),
    path("view_all_staff/",ViewStaff.as_view(),name="view_staff"),
    path('single_staff/<int:pk>/', StaffDetail.as_view(), name='single_staff_detail'),
    path('staff/delete/<int:pk>/', StaffDetail.as_view(), name='staff_detail_delete'),
    
    path('add_subject/', SubjectAddandView.as_view(),name="add_subject"),
    path('view_subject/', SubjectAddandView.as_view(),name="add_subject"),
    path('subject_update/<int:pk>/', SubjectUpdate.as_view(),name="update_subject"),
    path('subject_delete/<int:pk>/', SubjectDelete.as_view(),name="delete_subject"),
    
    path('add_session/', AddSession.as_view(),name="delete_subject"),
    path('all_session_year/',ViewAllSessionYear.as_view(),name="session_years"),
    path('session_year_update/<int:pk>/',UpdateDeleteSessionYear.as_view(),name="session_year_update"),
    path('session_year_delete/<int:pk>/',UpdateDeleteSessionYear.as_view(),name="session_year_delete"),
    
    
    
    
    #at send staff notification part first saw all staff then click on staff name and get notification page to send notification
    path("all_staff_with_notification_status/",ViewStaff_with_Notification_status.as_view(),name="see_all_staff_with_notification_status"),
    path("staff_notification/<int:pk>/",Send_Staff_Notification.as_view(),name="view_staff"),
    
    #staff leave view
    path("staff_leave_notification/",StaffApplyToLeave.as_view(),name="view_staff_leave"),
    path("staff_leave_approve/<int:pk>/",StaffLeaveApprove.as_view(),name="leave_approve"),
    path("staff_leave_disapprove/<int:pk>/",StaffLeaveDisApprove.as_view(),name="leave_disapprove"),
    
    
    
    path("view_all_staff_feedback/",StaffFeedback.as_view(),name="view_staff_feedback"),
    path("feedback_reply/<int:pk>/",StaffFeedbackReply.as_view(),name="staff_feedback_reply"),
    
    #see all student and send notification to the student
    path("get_all_student/",All_Student.as_view(),name="get_all_student"),
    path("send_student_notification/<int:pk>/",StudentNotification.as_view(),name="send_notification_to_student"),
    path("view_all_student_notification_history/",Student_Notification_History.as_view(),name="student_notification_history"),
    
    
    
    path("view_all_student_feedback/",StudentFeedback.as_view(),name="view_student_feedback"),
    path("student_feedback_reply/<int:pk>/",StudentFeedbackReply.as_view(),name="student_feedback_reply"),
    
    
    
    path("student_leave_notification/",StudentApplyToLeave.as_view(),name="view_student_leave"),
    path("student_leave_approve/<int:pk>/",StudentLeaveApprove.as_view(),name="leave_approve"),
    path("student_leave_disapprove/<int:pk>/",StudentLeaveDisApprove.as_view(),name="leave_disapprove"),
    
    
    
    
    
    
    
    
    
]
