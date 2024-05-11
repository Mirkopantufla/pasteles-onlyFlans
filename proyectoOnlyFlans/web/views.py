from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Flan, ContactForm
from .forms import ContactFormModelForm
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def indice(request):
    public_flans = Flan.objects.filter(is_private=False)
    context = {
        'public_flans':public_flans
    }
    return render(request, 'index.html', context)

def acerca(request):
    return render(request, 'about.html', {})

@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)
    context = {
        'private_flans':private_flans
    }
    return render(request, 'welcome.html', context)

def contacto(request):
    
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        #chequear que los datos son validos
        if form.is_valid():
            #Creamos los datos del formulario
            contact_form = ContactForm.objects.create(**form.cleaned_data) 
            return HttpResponseRedirect('/exito/')
    else:
        form = ContactFormModelForm()
    #el contexto, es el diccionario donde se envian los datos
    context = {'form':form}
    return render(request, 'contacto.html', context)

    
def exito(request):
    return render(request, 'exito.html')

def descripcion(request, flan_uuid):
    flan = Flan.objects.get(flan_uuid = flan_uuid)
    context = {'flan':flan}
    return render(request, 'descripcion.html', context)

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('/bienvenido/')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)

class MiVistaProtegida(LoginRequiredMixin, TemplateView):
    template_name = 'login.html'