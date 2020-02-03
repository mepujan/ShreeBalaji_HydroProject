from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField


# Create your models here.

class Gallery(models.Model):
    image = models.ImageField(upload_to='galleries')
    caption = models.CharField(max_length=50)
    publish_date = models.DateTimeField(default=now, blank=False)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = "Galleries"


class ProjectStatus(models.Model):
    status = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'ProjectStatus'

    def __str__(self):
        return self.status


class Project(models.Model):
    title = models.CharField(max_length=100)
    status = models.ForeignKey(ProjectStatus, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=now, blank=False)
    descriptions = RichTextField()

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'ContactUs'
