#iamthebest@123
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login
from django.urls import reverse

def home(request):
    return render(request , "index.html")
def prepython(request):
    return render(request , "prepython.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request ,"Successfully created.....")

        return redirect ('login')
    return render(request , "authentication/register.html")

def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request, "prepython.html", {'fname' : fname} )

        else:
            messages.error(request, "bad credential")
            return redirect('home')

    return render(request , "authentication/login.html")

def logout(request):

    return redirect(reverse('home'))