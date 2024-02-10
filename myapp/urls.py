from django.urls import path
from .views import *
urlpatterns = [
    path("login/",LoginAPIView.as_view(),name="login"),
    path("logout/",LogoutAPIView.as_view(),name="logout"),
    #you can update by put request and get profile by get request
    path("profile_get_and_update/",UserProfileAPIView.as_view(),name="profile_get_and_update"),
    
    
]
