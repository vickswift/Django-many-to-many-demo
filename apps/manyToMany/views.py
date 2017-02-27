from django.shortcuts import render, HttpResponse,redirect
from .models import User, Interest
from django.urls import reverse

# Create your views here.
def index(request):
    # return HttpResponse("Hello Victor!!")
    return render (request, 'manyToMany/index.html')

def add_user(request):     ####????
    if request.method != "POST":
        return redirect(reverse("index"))
    else:
        if User.objects.validateUser(request.POST):
            print("Went through", "*"*50)
            return redirect(reverse("showResults"))
        else:
            print ("didnt go through", "-"*50)
            return redirect(reverse('index'))

def show_results(request):
    context ={
    'users' : User.objects.all()
    }
    return render(request, 'manyToMany/results.html', context)

def show_interest(request, id):
    user = User.objects.filter(id=id)
    context = {
        'profile' : user[0].interests.all()
    }
    return render(request, 'manyToMany/interests.html', context)

def delete_interest(request, id):
    Interest.objects.get(id=id).delete()
    return redirect(reverse("showResults"))

def delete_user(request, id):
    User.objects.get(id=id).delete()
    return redirect(reverse("showResults"))
