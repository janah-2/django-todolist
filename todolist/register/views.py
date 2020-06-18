from django.shortcuts import render, redirect
from .forms import RegsiterForm

# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegsiterForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("/registered")


    else:
        form = RegsiterForm()
    return render(response, "register/register.html", {"form":form})
