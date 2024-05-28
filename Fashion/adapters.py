from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from .custom_social_models import SQLiteSafeSocialAccount

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_social_account(self, request, sociallogin, form=None):
        sociallogin.account.extra_data = {}
        sociallogin.account.save()
        return sociallogin.account