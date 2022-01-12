from django.shortcuts import render
from rest_framework.generics import  ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *




class Studentlist(ListCreateAPIView):#FOR GETTING ALL STUDENTS AND POST DATA
    queryset = Student.objects.all()
    serializer_class = Studentserializer


class PostDetail(RetrieveUpdateDestroyAPIView):#FOR GET PUT AND DELETE
    queryset = Student.objects.all()
    serializer_class = Studentserializer    



class Universitystudentlist(ListAPIView):#ACCEPTS THE UNIVERSITY ID AND GIVES THE STUDENTS
    serializer_class = Univstudentserializer 

    def get_queryset(self):
        univ_id =  self.kwargs['pk']
        return Student.objects.filter(university_id=univ_id)
