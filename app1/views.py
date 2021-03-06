from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return redirect('/')



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return render(request,'afterlogin.html')

        else:
            messages.info(request,'Username or Password is incorrect')


    return render(request,'login.html')




def register(request):
    form = CreateUserForm()

    if request.method == 'POST' :
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Account created for " + user)

            return redirect('login')


    context = {'form':form}
    return render(request,'register.html',context)



def afterLogin(request):
    return render(request,'afterlogin.html')

def Employeedata(request):
    return render(request,'regex.html')