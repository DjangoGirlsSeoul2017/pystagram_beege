from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model


def profile(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    ctx = {
        'user': user,
    }

    return render(request, 'profile.html', ctx)
