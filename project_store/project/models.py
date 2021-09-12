from django.db import models

# Create your models here.

class ProjectDetail(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField(max_length=1000)
    web_url=models.URLField(blank=True)
    yt_url=models.URLField(blank=True)
    yt_embed_url=models.URLField(blank=True)
    img=models.ImageField(upload_to='project')
    original_price=models.IntegerField()
    discounted_price=models.IntegerField()
    publish_date=models.DateTimeField()

    def __str__(self):
        return f'{self.id}-{self.title}'