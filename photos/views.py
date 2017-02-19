from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from .forms import PhotoForm
from django.shortcuts import get_object_or_404, redirect


def hello(request):
    return HttpResponse('안녕하세요!')


def detail(request, pk):
    try:
        photo = get_object_or_404(Photo, pk=pk)
    except Photo.DoesNotExist:
        return HttpResponse('Unable to find photo for that key')
    messages = (
        '<p>Primary key for photo is {pk}</p>'.format(pk=photo.pk),
        '<p>Photo address is {url}</p>'.format(url=photo.image.url),
        '<p><img src="{url}"></p>'.format(url=photo.image.url)
    )
    return HttpResponse('\n'.join(messages))


@login_required
def create(request):
    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)  # i don't know how this constructor works

        if form.is_valid():
            obj = form.save(commit=False)  # by saving the form, we get the Photo model back
            obj.user = request.user  # now we can assign the user
            obj.save()  # and save the Photo with the user

            return redirect(obj)

    ctx = {
        'form': form,
    }

    return render(request, 'edit.html', ctx)
