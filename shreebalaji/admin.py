from django.contrib import admin
from .models import Gallery, ProjectStatus, Project, ContactUs

# Register your models here.
admin.site.register(Gallery)
admin.site.register(ProjectStatus)
admin.site.register(Project)
admin.site.register(ContactUs)
