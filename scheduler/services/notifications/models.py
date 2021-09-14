from django.db import models

class Notifications(models.Model):
    medium_sent=models.CharField(max_length=255, null=True) 
    time_sent=models.CharField(max_length=5000, null=True)
    send_status=models.BooleanField(default=False)
#     is_twitter=models.BooleanField(default=False)
#     is_facebook=models.BooleanField(default=False)
#     is_linkedin=models.BooleanField(default=False)
#     datetime_to_publish=models.DateField()

#     def __str__(self):
#         return self.photo_id


