from django.shortcuts import render
from project.models import ProjectDetail
from django.views.generic import TemplateView
from django.views.generic.list import ListView

# Create your views here.

class HomeView(TemplateView):
    template_name='project/home.html'

class ProjectDetailListView(ListView):
    model=ProjectDetail