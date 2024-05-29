from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from userauths.forms import UserRegisterForm
from userauths.models import User

# Sign up view
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Your account {username} has been created successfully! You can now log in.')
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if new_user is not None:
                login(request, new_user)
                return redirect("core:index")
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, "userauths/login.html", context)

# Login view
def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in.")
        return redirect("core:index") 

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("core:index")
        else:
            messages.warning(request, "Invalid email or password.")

    return render(request, "userauths/login.html")

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("userauths:sign-in")
