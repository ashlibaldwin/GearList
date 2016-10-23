from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import redirect
from .models import List, Item, UserProfile
from .forms import ItemForm, ListForm, UserProfileForm, UserForm
from django.views.generic.edit import DeleteView # this is the generic view
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User


def home(request):
    return render(request, "gear/home.html", {})

def results(request):
    return render(request, "gear/results.html", {})

@login_required
def profile(request):
   #u = User.objects.get(username=request.user)

   #try:
     #user = UserProfile.objects.get(user=u)
   #except:
     #userprofile = None
     #http://www.dcs.gla.ac.uk/~leif/di/tutorial/tango-too.html

     return render(request, 'gear/profile.html', {})

@login_required
def list(request):
    username = None
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')

    elif request.user.is_authenticated:
       
        
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
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

            #login the new user automatically and redirect to homepage
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
          
            return HttpResponseRedirect("/")


        # Invalid form or forms - mistakes or something else?
        else:
            print (user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'gear/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):

    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        #email = request.POST['email']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/gear/list')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        return render(request, 'gear/login.html', {})

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')



