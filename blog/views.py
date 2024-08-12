from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
from django.db import models
import datetime
from django.views import View
from django.views.generic import ListView
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
    

def post_list(request):
    post_list = Post.published.all()
    #Pagination with 3 posts per page
    paginator = Paginator(post_list, 1)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request, 'blog/post/list.html', context = {"posts": posts})

def post_detail(request, id=None, **kwargs):
    if id != None:
        post = get_object_or_404(klass=Post.published, id = id)
    else:
        date = datetime.datetime(year = kwargs.get('year'), month = kwargs.get('month'), day = kwargs.get('day'))
        print(date)
        post = get_object_or_404(klass=Post.published, publish__year = date.year, publish__month=date.month, publish__day=date.day, slug=kwargs.get('slug'))
    return render(request, 'blog/post/detail.html', context={'post': post})

    # try:
    #     post = Post.published.get(id = id)
    # except Post.DoesNotExist:
    #     raise Http404("Post with such id didn't exist or is draft")
    
     
# def post_detail(request, year, month, day, slug):
#     date = datetime.datetime(year = year, month = month, day = day)
#     post = get_object_or_404(klass=Post.formated, publish = date, slug=slug)
#     return render(request, 'blog/post/detail.html', context={'post': post})
