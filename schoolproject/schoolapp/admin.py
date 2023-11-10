from django.contrib import admin

# # Register your models here

 # Register your models here.
from . models import Department, Course, Person, Purpose
#
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Person)
admin.site.register(Purpose)