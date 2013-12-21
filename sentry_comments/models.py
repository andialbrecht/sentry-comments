from django.conf import settings
from django.db import models

from sentry.models import Group


class GroupComments(models.Model):
    """Comment on group."""
    group = models.ForeignKey(Group)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
