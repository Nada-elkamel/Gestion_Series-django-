from .forms import FormConnexion
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User 
from .forms import FormUser

from MesSeries.models import Serie,Type
def index(request):
    ser = Serie.objects.all().values()
    type=Type.objects.all().values()
    template = loader.get_template('home.html')
    context = {
 'ser': ser,
 'type':type,
 }
    return HttpResponse(template.render(context, request))

def list_type(request):
    type=Type.objects.all().values()
    template = loader.get_template('types.html')
    context = {
 'type':type,
 }
    return HttpResponse(template.render(context, request))

def del_ser(request,id):
    serie = Serie.objects.get(id=id)
    serie.delete()
    return HttpResponseRedirect(reverse('series'))

def update_ser(request, id):
    ser = Serie.objects.filter(id=id).values().first()
    type=Type.objects.all().values()
    template = loader.get_template('updateSerie.html')
    context = {
    'ser': ser,
    'type':type, 
    }
    return HttpResponse(template.render(context, request))

def update_ser_action(request, id):
    nom = request.POST['nom']
    langue = request.POST['langue']
    typ=request.POST['type']
    type=Type.objects.all().get(id=typ)
    serie = Serie.objects.get(id=id)
    serie.nom = nom
    serie.langue =langue
    serie.type = type
    serie.save()
    return HttpResponseRedirect(reverse('series'))

def add(request):
    type = Type.objects.all().values()
    template = loader.get_template('addSerie.html')
    context = {
    'type': type,
    }
    return HttpResponse(template.render(context, request))
    
def add_ser(request):
    nom = request.POST['nom']
    langue = request.POST['langue']
    nbSaison = request.POST['nbSaison']
    dateDiffusion = request.POST['dateDiffusion']
    type = request.POST['type']
    type = Type.objects.get(id=type)
    serie = Serie(nom=nom, langue=langue, nbSaison=nbSaison, dateDiffusion=dateDiffusion,
    type=type)
    serie.save()
    return HttpResponseRedirect(reverse('series'))

def list_users(request):
    users = User.objects.all().values()
    template = loader.get_template('users.html')
    context = {
    'users':users,
    }
    return HttpResponse(template.render(context, request))

def del_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('users'))

def create_compte(request):
 user_form = FormUser ()
 return render(request, 'createUser.html', {'user_form' : user_form})
    
def create_user_action(request):
    adrEmail = request.POST['email']
    username = request.POST['login']
    password = request.POST['mot2pass']
    confirm = request.POST['confirm']
    prenom = request.POST['prenom']
    nom = request.POST['nom']
    if (password==confirm):
        user = User.objects.create_user(username, adrEmail,password)
        user.first_name = prenom
        user.last_name = nom
        user.save()
        return HttpResponseRedirect(reverse('users')) 
    else:
        print ("Mot de passe et confirmation mot de passe ne sont pas identiques")
        return HttpResponseRedirect(reverse('create_compte'))


def connect (request):
    connect_form = FormConnexion ()
    return render(request, 'connexion.html', {'connect_form' : connect_form,'error':False})

def signIn(request):
    
    username = request.POST['login']
    password = request.POST['mot2pass']
    #username = request.POST.get('login')
    #password = request.POST.get('mot2pass')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        request.session['username'] = username 
        return HttpResponseRedirect(reverse('series'))
 
    else:
        print("Login et/ou mot de passe incorrect")
        return render(request,'connexion.html', {'error':True,})
        #return HttpResponseRedirect(reverse('connect')) 
    
def signOut(request):
    logout(request) 
    return HttpResponseRedirect(reverse('connect'))

def update_user(request,id):
   user=User.objects.get(id=id)
   template=loader.get_template('UpdateUser.html')
   context={
       'user':user
   }
   return HttpResponse(template.render(context,request))

def update_user_action(request, id):
 user = User.objects.get(id=id)
 
 user.email = request.POST['email']
 user.username = request.POST['username']
#user.oldPassword = request.POST['oldPassword']
 user.password = request.POST['newPassword']
 user.first_name = request.POST['first_name']
 user.last_name = request.POST['last_name']
 user.save()
 return HttpResponseRedirect(reverse('users'))