from django.contrib import admin
from .models import University
from .models import UserData# Import your model

admin.site.register(University)
admin.site.register(UserData)# Register your model

