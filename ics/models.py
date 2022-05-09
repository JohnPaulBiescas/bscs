from re import X
from tkinter import CASCADE
from django.db import models

# Create your models here.


    
class Bscs1_2(models.Model):   
    idNumber = models.CharField(max_length=15)
    CC102 = models.FloatField()
    CS111 = models.FloatField()
    MATH103 = models.FloatField()
    resultCS12 = models.IntegerField()
    
class Bscs2_1(models.Model):
    idNumber = models.CharField(max_length=15)
    CC103 = models.FloatField()
    CS121 = models.FloatField()
    CS123 = models.FloatField()
    CS125 = models.FloatField()
    CS127 = models.FloatField()
    MATH104 = models.FloatField()
    resultCS21 = models.IntegerField()
    
class Bscs2_2(models.Model):
    idNumber = models.CharField(max_length=15)
    CC104 = models.FloatField()
    CS120 = models.FloatField()
    CS122 = models.FloatField()
    CS124 = models.FloatField()
    CS126 = models.FloatField()
    resultCS22 = models.IntegerField()

class Bscs3_1(models.Model):
    idNumber = models.CharField(max_length=15)
    CC105 = models.FloatField()
    CS131 = models.FloatField()
    CS135 = models.FloatField()
    CS137 = models.FloatField()
    resultCS31 = models.IntegerField()

class Bscs3_2(models.Model):
    idNumber = models.CharField(max_length=15)
    CS130 = models.FloatField()
    CS132 = models.FloatField()
    CS134 = models.FloatField()
    CS136 = models.FloatField()
    resultCS32 = models.IntegerField()
    
class Bsit1_1(models.Model):
    idNumber = models.CharField(max_length=15)
    CC100 = models.FloatField()
    CC101 = models.FloatField()
    resultIT11 = models.IntegerField()

class Bsit1_2(models.Model):
    idNumber = models.CharField(max_length=15)
    CC102 = models.FloatField()
    IT112 = models.FloatField()
    IT114 = models.FloatField()
    MATH103 = models.FloatField()
    resultIT12 = models.IntegerField()

class Bsit2_1(models.Model):
    idNumber = models.CharField(max_length=15)
    CC103 = models.FloatField()
    IT121 = models.FloatField()
    IT144 = models.FloatField()
    MATH104 = models.FloatField()
    resultIT21 = models.IntegerField()

class Bsit2_2(models.Model):
    idNumber = models.CharField(max_length=15)
    CC104 = models.FloatField()
    IT122 = models.FloatField()
    IT124 = models.FloatField()
    IT126 = models.FloatField()
    resultIT22 = models.IntegerField()

class Bsit3_1(models.Model):
    idNumber = models.CharField(max_length=15)
    CC105 = models.FloatField()
    IT131 = models.FloatField()
    IT133 = models.FloatField()
    IT135 = models.FloatField()
    IT137 = models.FloatField()
    resultIT31 = models.IntegerField()

class Bsit3_2(models.Model):
    idNumber = models.CharField(max_length=15)
    IT132 = models.FloatField()
    IT134 = models.FloatField()
    IT136 = models.FloatField()
    resultIT32 = models.IntegerField()

class Bscs1_1(models.Model):
    idNumber = models.CharField(max_length=15)
    CC100 = models.FloatField()
    CC101 = models.FloatField()
    resultCS11 = models.IntegerField()

class Totalit(models.Model):
    totalit = models.TextField()

class Totalcs(models.Model):
    totalcs = models.TextField()

class Course(models.Model):
    countcs = models.IntegerField()
    countit = models.IntegerField()