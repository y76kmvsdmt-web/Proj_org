from django.contrib import admin
from .models import *

admin.site.register([Department, Position, Employee, Customer, Project, Contract, Equipment, WorkGroup])