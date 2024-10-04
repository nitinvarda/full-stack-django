from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def studentsView(request):
    if request.method=="GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        
        return Response(serializer.data,status = status.HTTP_200_OK)
    elif request.method=="POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def studentDetailView(reqeust,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if reqeust.method=='GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status = status.HTTP_200_OK)
    elif reqeust.method=='PUT':
        serializer = StudentSerializer(student,data=reqeust.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif reqeust.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
