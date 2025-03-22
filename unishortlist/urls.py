from django.urls import path
from . import views
from django.shortcuts import render
from .views import add_university
from .views import uni_shortlist

# def forms(request):
#     return render(request, 'forms.html')
# def list(request):
#     return render(request, 'list.html')

urlpatterns = [

    path('sap/', views.adminpanel, name='adminpanel'),
    path('', views.home),
    path('forms/', views.forms, name='forms'),  # ✅ Corrected function reference
    path('list/', views.list, name='list'),  # ✅ Fixed incorrect reference
    path("adduni/", views.add_university, name="add_university"),
    path("uni_shortlist/", views.uni_shortlist, name="uni_shortlist"),

]