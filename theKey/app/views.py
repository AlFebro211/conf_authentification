from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages as ms
from django.contrib.auth import authenticate,login,logout

def home  (request):
   return render (request, 'index.html')


def registrer (request):
    if request.method == "POST":
        username = request.POST ['username']
        firstname = request.POST ['firstname']
        lastname = request.POST ['lastname']
        email = request.POST ['email']
        password = request.POST ['password']
        confirm_motpass = request.POST ['confirm password']
        mon_utilisateur = User.objects.create(username,email,password)
        mon_utilisateur.first_name = firstname
        mon_utilisateur.last_name = lastname 
        mon_utilisateur.save()
        ms.success(request, 'votre compte a ete cree avec succes ')
        return redirect ('login')        
    return render(request,'register.html')

def login (request):
    if request.method == "POST":
        username = request.POST ['username']
        password = request.POST ['password']
        user = authenticate(username=username, password = password)
        if user is not None:
            login(request,user)
            firstname = user.firstname
            return render(request,'login.html', {'firstname':firstname})
        else:
            ms.error(request,'Mauvaise authentification ')
            return redirect ('login')


def logout (request):
    pass