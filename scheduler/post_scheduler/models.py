from django.db import models

class Posts(models.Model):
    photo_id=models.CharField(max_length=11, primary_key=True, null=False, default=None)
    photo_url=models.CharField(max_length=255, null=True) 
    post_caption=models.CharField(max_length=5000, null=True)
    is_published=models.BooleanField(default=False)
    is_twitter=models.BooleanField(default=False)
    is_facebook=models.BooleanField(default=False)
    is_linkedin=models.BooleanField(default=False)
    datetime_to_publish=models.DateField()

    def __str__(self):
        return self.post_id


class Schedule(models.Model):
    post_id = models.CharField(max_length=11, null=False, default=None)
    scheduled_id = models.CharField(max_length=11, primary_key=True, null=False, default=None)

    def __str__(self):
        return self.post_id