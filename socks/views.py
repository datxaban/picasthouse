from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    socks_list = Sock.objects.all()
    context = {'socks':socks_list}
    return render(request,'socks/index.html',context)

def short(request):
    socks_list = Sock.objects.all().filter(isShort=True)
    result = "chua"
    if request.method == "POST":
        sort = Sort(request.POST)
        result = request.POST.get('choose', None)
        if result=="giam":
            socks_list = socks_list.order_by("-price")
        else:
            socks_list = socks_list.order_by("price")
        context = {'socks':socks_list,'sortresult':result}
        return render(request,'socks/short.html',context)
    context = {'socks':socks_list,'sortresult':result}
    return render(request,'socks/short.html',context)

def long(request):
    socks_list = Sock.objects.all().filter(isShort=False)
    print("wtf",socks_list)
    result = "chua"
    if request.method == "POST":
        sort = Sort(request.POST)
        if sort.is_valid():
            result = sort.cleaned_data['choice']
            if result=="giam":
                socks_list = socks_list.order_by("-price")
            else:
                socks_list = socks_list.order_by("price")
            context = {'socks':socks_list,'sortresult':result}
            return render(request,'socks/long.html',context)
    context = {'socks':socks_list,'sortresult':result}
    return render(request,'socks/long.html',context)
