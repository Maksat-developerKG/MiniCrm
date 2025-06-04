from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def index(request):
    return render(request=request,
                  template_name='main/index.html')


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request=request,
                  template_name='main/user_profile.html',
                  context={
                      'profile_user':user
                  })