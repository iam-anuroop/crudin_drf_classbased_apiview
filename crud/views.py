from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import Studentserilaiser
from .models import Student
from rest_framework.response import Response
from rest_framework import status




class Student_crud(APIView):
    def get(self,request,pk=None,format=None):

        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = Studentserilaiser(stu)
            return  Response(serializer.data)
        stu = Student.objects.all()
        serializer = Studentserilaiser(stu,many = True)
        return Response(serializer.data)
    

    def post(self,request,format=None):
        serialiser = Studentserilaiser(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response({'msg':'data created'},data=serialiser.data,status=status.HTTP_201_CREATED)
        return Response(serialiser.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def put(self,request,pk=None,format = None):
        id=pk
        stu = Student.objects.get(id=id)
        serialiser = Studentserilaiser(stu,data=request.data)
        
        if serialiser.is_valid():
            serialiser.save()
            return Response({'msg':'data updated'},data=serialiser.data)
        return Response(serialiser.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk=None,format=None):
        id=pk
        stu = Student.objects.get(id=id)
        serialiser = Studentserilaiser(stu,data=request.data,partial = True)
        if serialiser.is_valid():
            serialiser.save()
            return Response({'msg':'partialy updated'},data = serialiser.data)
        return Response(serialiser.errors,status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,pk=None,format = None):
        id=pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'data deleted'})
    


        


        




# Create your views here.
