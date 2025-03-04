from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

@method_decorator(csrf_exempt, name='dispatch')
class RegisterAPIView(APIView):
    # Optionally, disable authentication/permissions for login/registration
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(data=request.data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return Response({"success": True, "message": "Registration successful"})
        else:
            return Response({"success": False, "errors": form.errors}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return Response({"success": True, "message": "Login successful"})
        else:
            return Response({"success": False, "errors": form.errors}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class LogoutAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({"success": True, "message": "Logged out"})


class AuthStatusAPIView(APIView):
    permission_classes = [AllowAny]  # allow anyone to check auth status

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({
                "authenticated": True,
                "username": request.user.username
            })
        else:
            return Response({"authenticated": False})