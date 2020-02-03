from django.db import models


# Create your models here.
class Banner(models.Model):
    caption = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='Banners')

    def __str__(self):
        return self.caption
