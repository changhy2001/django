from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class AuthStatusAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({
                "authenticated": True,
                "username": request.user.username
            })
        else:
            return Response({"authenticated": False})