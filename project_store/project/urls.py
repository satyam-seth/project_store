from django.urls import path
from project import views

urlpatterns=[
    path('',views.ProjectDetailListView.as_view(),name='projectdetail_list'),
]