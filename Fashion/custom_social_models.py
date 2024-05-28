from django.db import models
from allauth.socialaccount.models import SocialAccount, SocialApp

class SQLiteSafeSocialAccount(SocialAccount):
    extra_data = models.TextField()

class SQLiteSafeSocialApp(SocialApp):
    extra_data = models.TextField()