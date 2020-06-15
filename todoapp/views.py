from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Todo
from . serializers import TodoSerializers
# Create your views here.

class todoList(APIView):
    def get(self, request):
        tasks=Todo.objects.all()
        serializer=TodoSerializers(tasks, many=True)
        return Response(serializer.data)

    def post(self):
        pass

def Intro(request):
    return HttpResponse("Welcome to my First DJANGO REST API.\n Try /tasks to view the JSON file")
