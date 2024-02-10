from django.urls import path
from student.views import *
urlpatterns = [
    path("view_My_notification/<int:pk>/",MyNotification.as_view(),name="view_My_notification"),
    path("notification_status_make_true/<int:pk>/",NotificationStatusChange.as_view(),name="notification_seen"),
    
    
    path("feedback_create/<int:pk>/",StudentFeedbackCreate.as_view(),name="create_feedback"),
    path("feedback_history/<int:pk>/",StudentFeedbackHistory.as_view(),name="feed_back_history"),
    
    
    #student apply for leave
    path("apply_leave_history/<int:pk>/",LeaveFromStudent.as_view(),name="leave_from_student"),
    path("leave_history/<int:pk>/",LeaveHistory.as_view(),name="leave_history_student"),
    
    
]