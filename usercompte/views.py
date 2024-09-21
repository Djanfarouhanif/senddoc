from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import SignupSerializer, SigninSerializer
from rest_framework.authtoken.models import Token
#creation de vue pour enregitré un utilisateur
class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Inscription réussie"}, status=status.HTTP_201_CREATED_SUCCESS)
   

#login user 
class SigninView(generics.GenericAPIView):
    serializer_class = SigninSerializer

    def post(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "user_id": user.id,
            "username": user.username
        })

class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
            return Response({"message": "Déconnexion réussie "}, status=status.HTTP_200_OK)

        except:
            return Response({"error": "problème lors de la déconnexion "}, status=status.HTTP_400_Request)