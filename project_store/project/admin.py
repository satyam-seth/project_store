from django.contrib import admin
from project.models import ProjectDetail

# Register your models here.

@admin.register(ProjectDetail)
class ProjectDetailAdmin(admin.ModelAdmin):
    list_display=['id','title','desc','web_url','yt_url','img','original_price','discounted_price','publish_date']