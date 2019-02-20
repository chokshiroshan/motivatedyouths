from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Article

#def Post(request):
    #return render(request,"templates/post.html",{})

def Contact(request):
    return render(request,"contact.html",{})

def About(request):
    return render(request,"about.html",{})

class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'
    ordering = ['-date_time']


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'post.html'
    context_object_name = 'thor'
