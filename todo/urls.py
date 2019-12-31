from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.index, name='index'),
    path('add',views.addTodo,name='add'),
    path('complete/<todo_id>',views.completeTodo,name='complete'),
    path('deleteComplete', views.deleteComplete,name='deleteComplete'),
    path('deleteAll', views.deleteAll,name='deleteAll')
]