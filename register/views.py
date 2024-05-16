from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.




def index(request):

    if request.method == 'POST':
        Firstname = request.POST['Firstname']

        password = request.POST['password']

        user = authenticate(username = Firstname, password =password  )

        if user is not None:
            login(request , user)
            return redirect('/home')
        else:
            messages.info(request, 'invalid Firstname or password')
            return redirect("/")
    else:
        return render(request,'index.html')


def register(request):

    if request.method == 'POST':

        email = request.POST['email']
        Firstname = request.POST['Firstname']
        password= request.POST['password']
        birthdate = request.POST['birthdate']
        Lastname = request.POST['Lastname']



        user = User.objects.create_user(username = Firstname , password = password , email = email)
        user.save()
        print('user created')
        return redirect('/custom')

    return render(request,'register.html')


def custom(request):
    return render(request, 'custom.html')


def home(request):
    return render(request, 'homepage.html')