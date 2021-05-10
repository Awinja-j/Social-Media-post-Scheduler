from django.db import models

class LongLivedAccessToken(models.Model):
    access_token = models.CharField(max_length=500, primary_key=True, null=False, default=None)
    token_type = models.CharField(max_length=500)
    expires_in = models.DateField(default=False)
    date_created = models.DateField(default=False)

    def __str__(self):
        return self.access_token