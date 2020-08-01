from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

def Index(request):
    return HttpResponseRedirect(reverse('app_blog:blog_list'))