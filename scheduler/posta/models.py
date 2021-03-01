from django.db import models

# Create your models here.
class Posts(models.Model):
    image_url=models.CharField(max_length=200,blank=False, default=None)
    caption=models.CharField(max_length=200,blank=False, default=None)
    published=models.BooleanField(default=False)
    platform_to_publish=models.CharField(max_length=200,blank=False, default=None)
    date_to_be_published=models.DateField()

