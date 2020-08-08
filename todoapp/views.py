from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ListItem, List
from django.contrib.auth.models import User

def todoapp(request, list_id):   
        try:
            target_list = List.objects.get(id = list_id) # The list to which the item has to be added
            print(target_list)
            all_todo_items=ListItem.objects.filter(list_id = target_list)
            #all_todo_items=ListItem.objects.all()
            print(all_todo_items)
            return render(request, 'todoapp/home.html',{'all_items':all_todo_items})
        except:
            print(request.user.id)
            context = {'list':List.objects.get(id = list_id)}
            return render(request, 'todoapp/home.html', context)

def addItem(request, list_id):
    new_todo_item = request.POST.get("todoitem")
    target_list = List.objects.get(id = list_id) # The list to which the item has to be added
    print(new_todo_item)
    ListItem.objects.create(name = new_todo_item, list_id = target_list)
    return redirect('todoapp_home',list_id)

def delItem(request, todo_id):
    item = ListItem.objects.get(id = todo_id)
    item_list = item.list_id.id
    item.delete()
    return redirect('todoapp_home',item_list)

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