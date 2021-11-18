from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    return render(request,'accounts/profile.html')

def user_login(request):
    if request.method == "POST":
        # if not request.user.is_authenticated:
        #     return redirect('accounts:login')
        # else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('accounts:profile')
        else:
            return render(request, "accounts/login.html", context={"message": "invalid username or passowrd"})

    return render(request,'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('accounts:profile')

def signup(request):
    form = UserCreationForm(request.POST or None)
    template_name = 'accounts/signup.html'
    # success_url = reverse_lazy( 'movies:index' ) 
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            return redirect('movies:index')
    return render(request , template_name , context={'form': form})