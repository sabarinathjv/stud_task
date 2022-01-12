
from django.urls import path
from .views import *

urlpatterns = [
      path('students', Studentlist.as_view(), name='students'),
      path('studoperation/<int:pk>/', PostDetail.as_view(), name='studoperation'),
      path('university/<int:pk>/', Universitystudentlist.as_view(), name='stud_list'),


      

]
