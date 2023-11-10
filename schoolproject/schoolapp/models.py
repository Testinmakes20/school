from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Course(models.Model):
    department= models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
class Purpose(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=124)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=15)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=150)
    address=models.CharField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    purpose = models.ForeignKey(Purpose,on_delete=models.SET_NULL,blank=False,null=True)

    def __str__(self):
        return self.name



# Create your models here.
