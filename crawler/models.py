from django.db import models

# Create your models here.
class CrawlerArticle(models.Model):
    title = models.CharField(max_length=50)
    language = models.CharField(max_length=50, default='한자')
    photo = models.ImageField(blank=False, upload_to='crawler/%Y/%m/%d')
    cdate = models.DateTimeField(auto_now_add=True)