from django.db import models
# from django.contrib.auth.models import User
# from shelf.models import BookItem
from django.utils.timezone import now
from django.conf import settings


class Rental(models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL)
    what = models.ForeignKey('shelf.BookItem')
    when = models.DateTimeField(default=now)
    returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'self.what'  # zadanie domowe