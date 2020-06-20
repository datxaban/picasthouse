from rest_framework import serializers
from .models import Sock

class SockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sock
        # fields = '__all__'
        fields = ('name','title','isLeft','isNew','isShort','isHot','price')