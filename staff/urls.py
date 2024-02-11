from django.urls import path
from staff.views import *
urlpatterns = [ 
    #you can use one
    path("view_notification/",MyNotification.as_view(),name="view_staff_notification"),
    path("view_notification/<int:pk>/",MyNotification.as_view(),name="view_staff_notification"),
    
    
    path("notification_status_make_true/<int:pk>/",NotificationStatusChange.as_view(),name="view_staff_notification"),
    
    #staff apply for leave
    path("leave_history/<int:pk>/",LeaveHistory.as_view(),name="leave_history_staff"),
    path("apply_leave_history/<int:pk>/",LeaveFromStaff.as_view(),name="leave_from_staff"),
    
    path("feedback_create/<int:pk>/",FeedbackCreate.as_view(),name="create_feedback"),
    path("feedback_history/<int:pk>/",FeedbackHistory.as_view(),name="feed_back_history"),
    
    #view all subjects of staff using id and get the all session year
    path("subjects_and_session_year/<int:pk>/",SubjectsAndSessionYear.as_view(),name="subjects_and_session_year"),
    
    
]