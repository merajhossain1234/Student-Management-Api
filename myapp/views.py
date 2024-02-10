from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, login,logout
from  .serializers import CustomUserSerializer


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = EmailBackend.authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            user_type = user.user_type

            if user_type == 1:
                
                return Response({'message': 'Login successful and this is HOD pannel'}, status=status.HTTP_200_OK)
            elif user_type == 2:
                return Response({'message': 'Login successful and this is STAFF pannel'}, status=status.HTTP_200_OK)
            elif user_type == 3:
                return Response({'message': 'Login successful and this is STUDENT pannel'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'INVALID user type'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
 
 
        
class UserProfileAPIView(APIView):
    def get(self, request, format=None):
        # Get the current user
        user = request.user

        # Serialize the user profile data
        serializer = CustomUserSerializer(user)

        return Response(serializer.data)

    def put(self, request, format=None):
        # Get the current user
        user = request.user

        # Deserialize the request data
        serializer = CustomUserSerializer(user, data=request.data,instance=user)

        if serializer.is_valid():
            # Save the updated user profile
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       


        
class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)