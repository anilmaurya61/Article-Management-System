from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token



class UserCreateView(APIView):
    """
    Handle user registration.
    """
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(APIView):
    """
    List all users (for testing purposes, restricted in production).
    """
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class LoginView(APIView):
    """
    Handle user login and return authentication token.
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'message': 'Login successful', 'role': user.role, 'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    """
    Handle user logout by invalidating the token.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # If the user is not authenticated, return an error response
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication credentials were not provided.'},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Delete the user's token
        Token.objects.filter(user=request.user).delete()
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)


class PasswordChangeView(APIView):
    """
    Handle password change for authenticated users.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        # Validate old password
        if not request.user.check_password(old_password):
            return Response({'error': 'Old password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)

        # Set the new password
        request.user.set_password(new_password)
        request.user.save()
        return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)