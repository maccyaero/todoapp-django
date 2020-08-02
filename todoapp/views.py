from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ListItem

def home(request):     
    all_todo_items=ListItem.objects.all()
    return render(request, 'todoapp/home.html',{'all_items':all_todo_items})

def addItem(request):
    new_todo_item = request.POST.get("todoitem")
    print(new_todo_item)
    ListItem.objects.create(name = new_todo_item)
    return redirect('todoapp_home')

def delItem(request, todo_id):
    ListItem.objects.get(id = todo_id).delete()
    return redirect('todoapp_home')
       

#def about(request):
	#return render(request,'blog/about.html',{"title":"About"})