"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todoapp import views
from register import views as register_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp/<int:list_id>', views.todoapp, name ='todoapp_home'),
    path('addItem/<int:list_id>', views.addItem, name ='todoapp_add'),
    path('delItem/<int:todo_id>', views.delItem, name ='todoapp_del'),
    path('delList/<int:list_id>', views.delList, name ='todoapp_delList'),
    path('', register_views.register,name='todoapp-register'),
    path('loginPage/',register_views.loginPage,name='todoapp-login'),
    path('createList/',views.createList,name='todoapp-createList'),
    path('addList/',views.addList,name='todoapp-addList'),
]
