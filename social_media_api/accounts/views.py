from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from .serializers import UserLoginSerializer
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
# import RefreshToken # type: ignore
# from rest_framework_simplejwt.token import RefreshToken

# Create your views here.
class UserRegistrationView(APIView):
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
              "message": "User registered successfully"
            }, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        # refresh = RefreshToken.for_user(user)
        # return Response({
        #     'refresh': str(refresh),
        #     'access': str(refresh.access_token),})
        
class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
            
class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_to_follow = User.objects.get(username=kwargs['username'])
        if user_to_follow == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_to_unfollow = User.objects.get(username=kwargs['username'])
        if user_to_unfollow == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)

    