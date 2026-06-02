from django.urls import path
from studentapp.views import *

urlpatterns = [
     path('',SignUpView.as_view(),name='signup'),
     path('shome',StudentHomeView.as_view(),name='shome'),
     path('addstudent',AddStudentView.as_view(),name='addstudent'),
     path('editstudent/<int:id>',EditStudentView.as_view(),name='editstudent'),
     path('deletestudent/<int:id>',DeleteStudentView.as_view(),name="deletestudent")
   
  
  
]