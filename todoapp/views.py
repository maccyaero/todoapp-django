from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ListItem, List
from django.contrib.auth.models import User

def todoapp(request, list_id):     
    all_todo_items=ListItem.objects.get(list_id = list_id)
    return render(request, 'todoapp/home.html',{'all_items':all_todo_items})

def addItem(request, list_id):
    new_todo_item = request.POST.get("todoitem")
    print(new_todo_item)
    ListItem.objects.create(name = new_todo_item)
    return redirect('todoapp_home')

def delItem(request, todo_id):
    ListItem.objects.get(id = todo_id).delete()
    return redirect('todoapp_home')

def createList(request):
    context = {'lists':List.objects.all()}
    return render(request, 'todoapp/lists.html',context)

def addList(request):
    listname = request.POST.get("list")
    user_id = request.user.id
    user = User.objects.get(id = user_id)
    List.objects.create(name = listname, user_id = user)
    return redirect('todoapp-createList')
    
def delList(request, list_id):
    List.objects.get(id = list_id).delete()
    return redirect('todoapp-createList')
       

#def about(request):
	#return render(request,'blog/about.html',{"title":"About"})