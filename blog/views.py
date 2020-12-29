from django.shortcuts import render,HttpResponse
from blog.models import Postblog

# Create your views here.
def blogHome(request):
    allposts = Postblog.objects.all()
    context = {'allposts':allposts}
    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    post= Postblog.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request,'blog/blogPost.html',context)

