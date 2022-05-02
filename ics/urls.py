from django.urls import include, path
from django.shortcuts import redirect

from .views import index,CSpage,ITpage,CS1_2page,CS2page,CS2_2page,CS3page,IT1_2page,IT2page,IT2_2page,IT3page,CS3_2page,IT3_2page,resultCS1_1,resultCS1_2,resultCS2_1,resultCS2_2,resultCS3_1,resultCS3_2,resultIT1_1,resultIT1_2,resultIT2_1,resultIT2_2,resultIT3_1,resultIT3_2,tableCS12,deleteCS12,tableCS21,deleteCS21,deleteCS22,tableCS22,tableCS31,deleteCS31,tableCS32,deleteCS32,tableCS41,deleteCS41,tableIT12,deleteIT12,tableIT21,deleteIT21,tableIT22,deleteIT22,tableIT31,deleteIT31,tableIT32,deleteIT32,deleteIT41,tableIT41


from . import views

urlpatterns = [ 
    path('', index, name="index"),
    path('CSpage', CSpage, name = "CSpage"),
    path('CS1_2page', CS1_2page, name = "CS1_2page"),
    path('CS2page', CS2page, name = "CS2page"),
    path('CS2_2page', CS2_2page, name = "CS2_2page"),
    path('CS3page', CS3page, name = "CS3page"),
    path('CS3_2page', CS3_2page, name = "CS3_2page"),
    path('ITpage', ITpage, name = "ITpage"),
    path('IT1_2page', IT1_2page, name = "IT1_2page"),
    path('IT2page', IT2page, name = "IT2page"),
    path('IT2_2page', IT2_2page, name = "IT2_2page"),
    path('IT3page', IT3page, name = "IT3page"),
    path('IT3_2page', IT3_2page, name = "IT3_2page"),
    
    path('resultCS1_1', resultCS1_1, name = "resultCS1_1"),
    path('resultCS1_2', resultCS1_2, name = "resultCS1_2"),
    path('resultCS2_1', resultCS2_1, name = "resultCS2_1"),
    path('resultCS2_2', resultCS2_2, name = "resultCS2_2"),
    path('resultCS3_1', resultCS3_1, name = "resultCS3_1"),
    path('resultCS3_2', resultCS3_2, name = "resultCS3_2"),
    
    path('resultIT1_1', resultIT1_1, name = "resultIT1_1"),
    path('resultIT1_2', resultIT1_2, name = "resultIT1_2"),
    path('resultIT2_1', resultIT2_1, name = "resultIT2_1"),
    path('resultIT2_2', resultIT2_2, name = "resultIT2_2"),
    path('resultIT3_1', resultIT3_1, name = "resultIT3_1"),
    path('resultIT3_2', resultIT3_2, name = "resultIT3_2"),
    
    path('tableCS12', tableCS12, name = "tableCS12"),
    path('tableCS21', tableCS21, name = "tableCS21"),
    path('tableCS22', tableCS22, name = "tableCS22"),
    path('tableCS31', tableCS31, name = "tableCS31"),
    path('tableCS32', tableCS32, name = "tableCS32"),
    path('tableCS41', tableCS41, name = "tableCS41"),
    path('tableIT12', tableIT12, name = "tableIT12"),
    path('tableIT21', tableIT21, name = "tableIT21"),
    path('tableIT22', tableIT22, name = "tableIT22"),
    path('tableIT31', tableIT31, name = "tableIT31"),
    path('tableIT32', tableIT32, name = "tableIT32"),
    path('tableIT41', tableIT41, name = "tableIT41"),
    
    path('deleteCS12/<student_id>', deleteCS12, name = "deleteCS12"),
    path('deleteCS21/<student_id>', deleteCS21, name = "deleteCS21"),
    path('deleteCS22/<student_id>', deleteCS22, name = "deleteCS22"),
    path('deleteCS31/<student_id>', deleteCS31, name = "deleteCS31"),
    path('deleteCS32/<student_id>', deleteCS32, name = "deleteCS32"),
    path('deleteCS41/<student_id>', deleteCS41, name = "deleteCS41"),
    path('deleteIT12/<student_id>', deleteIT12, name = "deleteIT12"),
    path('deleteIT21/<student_id>', deleteIT21, name = "deleteIT21"),
    path('deleteIT22/<student_id>', deleteIT22, name = "deleteIT22"),
    path('deleteIT31/<student_id>', deleteIT31, name = "deleteIT31"),
    path('deleteIT32/<student_id>', deleteIT32, name = "deleteIT32"),
    path('deleteIT41/<student_id>', deleteIT41, name = "deleteIT41"),
]
