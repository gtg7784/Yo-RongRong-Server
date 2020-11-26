from django.core.files.storage import FileSystemStorage
from django.db import models

fs_log = FileSystemStorage(location="media/log/")
fs_data = FileSystemStorage(location="media/data/")


class Img(models.Model):
    id = models.CharField(max_length=200, auto_created=True, primary_key=True)
    image = models.ImageField(storage=fs_data)
    name = models.CharField(max_length=200)
    related_links = models.CharField(max_length=200, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id


class Log(models.Model):
    id = models.CharField(max_length=200, auto_created=True, primary_key=True)
    phone_id = models.CharField(max_length=200)
    image = models.ImageField(storage=fs_log)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
