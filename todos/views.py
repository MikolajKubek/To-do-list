from django.shortcuts import render
from django.urls import reverse 
from django.http import HttpResponseRedirect, JsonResponse

from .forms import TodoForm, LoginForm
from .models import Todo

from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home_view(request):
    if request.user.is_authenticated:
        form = TodoForm()
        object_list = Todo.objects.filter(author=request.user)
        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                Todo.objects.create(content=form.cleaned_data.get('content'), date=form.cleaned_data.get('date'), author=request.user)
                form = TodoForm()
                return HttpResponseRedirect(reverse('todos:home_view'))
        context = {
            'form': form,
            'object_list': object_list,
        }
        return render(request, 'todos/home.html', context)
    else:
        return HttpResponseRedirect(reverse('todos:login'))


def delete_todo(request, id):
    if request.method == 'POST':
        obj = Todo.objects.get(id=id)
        if obj != None:
            if obj.author == request.user:
                obj.delete()
            else:
                return JsonResponse({'delete_todo': 'unauthorized'})
        else:
            return JsonResponse({'delete_todo': 'no such object in database'})
            
    return JsonResponse({'delete_todo': 'success'})


def switch_state(request, id):
    if request.method == 'POST':
            obj = Todo.objects.get(id=id)
            if obj != None:
                if obj.author == request.user:
                    obj.completed = not obj.completed
                    obj.save()
                else:
                    return JsonResponse({'switch_state': 'nieupowazniony'})
            else:
                return JsonResponse({'switch_state': 'no such object in database'})
  
    return JsonResponse({'switch_state': 'success'})

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(request.POST['username'])
            user = authenticate(request, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('todos:home_view'))
            else:
                return HttpResponseRedirect(reverse('todos:login'))
    context = {
        'form': form,
    }

    return render(request, 'todos/login.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'todos/logout.html')



    