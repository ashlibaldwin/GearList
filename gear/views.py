from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from .models import List, Item, UserProfile
from .forms import ItemForm, ListForm, UserProfileForm, UserForm
from django.views.generic.edit import DeleteView # this is the generic view
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User


def home(request):
    return render(request, "gear/home.html", {})


@login_required
def profile(request):
     return render(request, 'gear/profile.html', {})


@login_required
def list(request):
    username = None
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.user.is_authenticated:
        lists = List.objects.filter(user=request.user)
        form = ListForm(request.POST or None)
        if request.method == "POST":
            form = ListForm(request.POST)
            if form.is_valid():
                list = form.save(commit=False)
                list.user = request.user
                list.save()
                return redirect('gear:list_detail', pk=list.pk)
    else:
        form = ListForm()

    return render(request, 'gear/list.html', {'lists': lists, 'form': form})

@login_required
def list_detail(request, pk):
    lists = List.objects.get(user=request.user, pk=pk)
    items =lists.item_set.all()
    form = ItemForm
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.todo_list = lists
            item.save()
            form = ItemForm
            return redirect('gear:list_detail', pk=pk)
    else:
        form = ItemForm()

    return render(request, 'gear/list_detail.html', {'items': items, 'form': form, 'lists':lists})


def delete_list(request, pk):
    list = get_object_or_404(List, pk=pk)
    if request.method=='POST':
        list.delete()
        return redirect('gear:list')

    return render(request, 'gear/delete_list.html', {'object':list})


def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method=='POST':
        item.delete()
        list_id = item.todo_list.id
        list_url = "/gear/list_detail/" +str(list_id)
        return redirect(list_url)
    
    return render(request, 'gear/delete_item.html', {'object':item})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
            username = request.POST['username']
            password = request.POST['password']
            login(request, user)
          
            return HttpResponseRedirect("/")
        else:
            print (user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'gear/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        #email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/gear/list')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print ("Invalid login details")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'gear/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
