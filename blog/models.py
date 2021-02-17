import base64
import uuid

from django.db import models
from django.conf import settings
from django.utils import timezone
from bulbasaursblog.utils import api_utils


class Post(models.Model):
    sguid = api_utils.generate_short_guid_with_prefix(prefix='post')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.sguid
