from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('short',views.short,name="short"),
    path('long',views.long,name="long"),
    # path('sortshort',views.sortshort,name="sortshort")
]
