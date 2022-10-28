from lib2to3.pgen2 import token
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
    return Response(data="Only for logged in user", status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userInfo(request, format=None):
    content = {
        'id': str(request.user.id),
        'email': str(request.user.email),
        'phone': str(request.user.phone),
        'first_name' : str(request.user.first_name),
        'last_name' : str(request.user.last_name),
        'username' : str(request.user.username)
    }
    
    return Response(content)