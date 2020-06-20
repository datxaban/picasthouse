from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SockSerializer
from .models import Sock
# from .models import *
from .forms import *
from  rest_framework import status
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


@api_view(['GET'])
def api(request):
    api_urls ={
        'List':'api/sock-list',
        'Add':'api/sock-add',
        'Update':'api/sock-update/<str:name>',
        'Delete':'api/sock-delete/<str:name>',
    }
    return Response(api_urls)

@api_view(['GET'])
def sockList(request):
    sockList = Sock.objects.all()
    sockListApi = SockSerializer(sockList,many=True)
    return Response(sockListApi.data)

@api_view(['POST'])
def sockAdd(request):
    serializer = SockSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def sockDel(request,name):
    delSock = Sock.objects.all().filter(name=name)
    delList = list(delSock)
    if len(delList)==0:
        return Response(status=status.HTTP_404_NOT_FOUND)
    for x in delList:
        x.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def sockUpdate(request,name):
    sock = Sock.objects.all().filter(name=name)
    sockList = list(sock)
    if len(sockList) == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = [SockSerializer(instance=sock,data=request.data) for sock in sockList]
    for x in serializer:
        if x.is_valid():
            x.save()
        else:
            return Response("Wrong data",status=status.HTTP_400_BAD_REQUEST)
    return Response([x.data for x in serializer])
