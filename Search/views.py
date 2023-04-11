from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView
from .models import Student
from .serializer import StudentSerializer
from rest_framework import filters
from rest_framework import generics
from django.http import HttpResponse
#from django.db.models import Avg
from django.db.models import Avg, Max, Min
class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    #max =queryset.aaggregate(Max("marks"))


def Aggregate(request):
    
        max = Student.objects.aggregate(Max("marks"))
     #   print(stu.values())
        min = Student.objects.aggregate(Min("marks"))
        avg = Student.objects.aggregate(Avg("marks"))
        
        return HttpResponse(f'{max}   {min}  {avg}')
      
     
#>>> Book.objects.
        #     stu = Student.objects.all()  #filter(pk=pk)
            
        #     stuSerializer =StudentSerializer(stu, many=True)
        #     return Response(stuSerializer.data)
            
        

