from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, advisorsSerializer, BookingSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from . models import advisors
from . models import booking
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer

from rest_framework.authtoken.models import Token
from knox.views import LoginView as KnoxLoginView

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        # "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1],
        "User_id": serializer.instance.id
        })



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        # return super(LoginAPI, self).post(request, format=None)
        
        Response = super(LoginAPI, self).post(request, format=None)
        token, created = Token.objects.get_or_create(user_id=user.id)
        
        Response.data["user_id"] = user.id
        return Response


class advisorList(APIView):
    def get(self, request, userid):
        advisorone=advisors.objects.all()
        serializer=advisorsSerializer(advisorone, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class BookingAPI(generics.GenericAPIView):
    serializer_class = BookingSerializer
    def post(self, request,userid,advisorid, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.save()
        return Response({
            "userid": userid,
           " advisorid": advisorid
        })