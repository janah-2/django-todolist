from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    
                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                
                else:
                    print("Invalid")

        return render(response, 'main/list.html', {"ls":ls})
    return render(response, 'main/view.html', {})

def home(response):
    return render(response, 'main/home.html', {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
    
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" %t.id)
    
    else:
        form = CreateNewList()

    return render(response, 'main/create.html', {"form":form})

def registered(response):
    return render(response, 'register/registered.html', {})

def loggedin(response):
    return render(response, 'register/loggedin.html', {})

def loggedout(response):
    return render(response, 'register/loggedout.html', {})

def view(response):
    return render(response, 'main/view.html', {})

def deleteList(response, pk):
    items = ToDoList.objects.get(id=pk)

    if response.method == "POST":
        items.delete()
        return redirect('/view')

    return render(response, 'main/deletelists.html', {'items':items})

def deleteTask(response, pk, id):
    items = ToDoList.objects.get(id=pk)
    item_1 = items.item_set.get(id=id)

    if response.method == "POST":
        item_1.delete()
        return redirect("/%i" %items.id)

    return render(response, 'main/delete.html', {"item_1":item_1, "items":items})