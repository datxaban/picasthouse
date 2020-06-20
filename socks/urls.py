from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('short',views.short,name="short"),
    path('long',views.long,name="long"),
    path('api',views.api,name="api"),
    path('api/sock-list',views.sockList,name="list"),
    path('api/sock-add',views.sockAdd,name="add"),
    path('api/sock-delete/<str:name>',views.sockDel,name="delete"),
    path('api/sock-update/<str:name>',views.sockUpdate,name="update")
]
