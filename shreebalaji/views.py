from django.contrib import messages
from django.shortcuts import render
from django.views import View
from cms.models import Banner
from .models import Gallery, Project
from .form import ContactUsForm
from django.shortcuts import get_object_or_404


# Create your views here.
class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


def index(request):
    banners = Banner.objects.all()
    context = {
        'banners': banners
    }
    return render(request, 'index.html', context)


def galleries(request):
    images = Gallery.objects.order_by('-publish_date')
    context = {
        'images': images
    }
    return render(request, 'galleries.html', context)


class Services(View):
    template_name = 'services.html'

    def get(self, request):
        return render(request, self.template_name)


class ContactUs(View):
    template_name = 'contactus.html'

    def get(self, request):
        form = ContactUsForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been recorded Successfully.')
        else:
            messages.error(request, 'Error in submitting the message. Try Again... ')
        return render(request, self.template_name, {'form': form})


class AboutUs(View):
    template_name = 'aboutus.html'

    def get(self, request):
        return render(request, self.template_name)


class Ongoing(View):
    template_name = 'ongoingproject.html'

    def get(self, request):
        project = Project.objects.filter(status__status__icontains='ongoing').order_by('-publish_date')
        return render(request, self.template_name, {'project': project})


class Completed(View):
    template_name = 'completedproject.html'

    def get(self, request):
        project = Project.objects.filter(status__status__icontains='completed').order_by('-publish_date')
        return render(request, self.template_name, {'project': project})
