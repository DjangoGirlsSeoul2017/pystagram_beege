from django.db import models


class Photo(models.Model):
    id = models.UUIDField()
    image = models.ImageField()
    filtered_image = models.ImageField()
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
