from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import render


class MyAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return False

class MySocialAccount(DefaultSocialAccountAdapter):
    allowed_users = ["pratinavmongia@gmail.com", "chaitanyaiyer01@gmail.com", "f20200012@pilani.bits-pilani.ac.in"]
    def is_open_for_signup(self, request, sociallogin):
        return True

    def pre_social_login(self, request, sociallogin):
        try:
            u = sociallogin.user
            if u.email not in self.allowed_users:
                raise ImmediateHttpResponse(render(request, '403.html'))
        except:
            raise ImmediateHttpResponse(render(request, '403.html'))
            