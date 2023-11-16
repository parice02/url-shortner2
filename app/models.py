from django.db import models

# Create your models here.


class URLShort(models.Model):
    long_url = models.URLField()
    short_url = models.URLField()
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
