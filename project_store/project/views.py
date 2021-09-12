from project.models import ProjectDetail
from django.views.generic.list import ListView

# Create your views here.

class ProjectDetailListView(ListView):
    model=ProjectDetail
    paginate_by=5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projectdetail_active"] = 'active'
        return context