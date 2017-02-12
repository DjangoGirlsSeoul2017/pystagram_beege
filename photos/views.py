from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from .forms import PhotoForm
from django.shortcuts import get_object_or_404


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


def create(request):
    form = PhotoForm()
    ctx = {
        'form': form,
    }
    return render(request, 'edit.html', ctx)
