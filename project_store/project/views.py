from project.models import ProjectDetail
from django.views.generic.list import ListView

# Create your views here.

class ProjectDetailListView(ListView):
    model=ProjectDetail