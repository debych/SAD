from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your views here.
def index(request):
    context = {}
    return render(request, 'docs/index.html', context)

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        user = User.objects.get(username=request.POST.get('username'))
        default_group = Group.objects.get(name='default')
        user.groups.add(default_group)
        user.is_staff = True
        user.save()
        return redirect('/admin')

    context = {'form': form}
    return render(request, 'docs/register.html', context)