from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Postblog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
#check the length of the contact us form
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            #error message import
            messages.error(request,'Please fill the form correctly')
        else:    
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,'Your form has been submitted successfully We will contact you soon.')
    return render(request, "home/contact.html")

def search(request):
    query = request.GET['query']
    #for none query set
    if len(query)>233:
        allposts=Postblog.objects.none()
    #To fetch the data in search
    else:
        allpostsTitle = Postblog.objects.filter(title__contains=query)
        allpostsContent = Postblog.objects.filter(content__contains=query)
        allposts= allpostsTitle.union(allpostsContent)
    if allposts.count() == 0:
        messages.warning(request,'Your search not found ')
    params={'allposts':allposts, 'query':query}
    return render(request,'home/search.html',params)
    
# Handle authentication
def handleSignup(request):
    if request.method == 'POST':
        # for user 
        # must match id that you are called like 'fname' that is present in base.html is same as ['fname'] 
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        #checks for errorneous input
        # username must be under 10 character
        if len(username) > 10:
            messages.error(request,'Username must be under 10 character ')
            return redirect('/')
        # username must be alphanumeric
        # if username.isalnum():
        #     messages.error(request,'username contain only letters and numbers ')
        #     return redirect('home')
        # Password do not match
        if pass1 != pass2:
             messages.error(request,'Password do not match ')
             return redirect('/')
        
        # create the user and save user data in database
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'Woohoo! Account successfully created ')
        # import redirect from shortcuts
        return redirect('/')



    else:
        return HttpResponse('404 - ERROR')

def handleLogin(request):

    if request.method == 'POST':
        # for user 
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,'Login successfully  ')
            return redirect('/')
        else:
             messages.error(request,'Invalid Credentials ')
             return redirect('/')
    return HttpResponse('404 - ERROR')

def handleLogout(request):
    logout(request)
    messages.success(request,'Successfully Logged Out ')
    return redirect('/')
    
          