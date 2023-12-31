from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader

from .models import Post
from django.views.generic import TemplateView
# Create your views here.

# class portfolioview(TemplateView):
#     template_name = 'portfolio.html'


class members(TemplateView):
    template_name = 'portfolio.html'

# def ok(request):
#     return render(request,'portfolio.html') 

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

