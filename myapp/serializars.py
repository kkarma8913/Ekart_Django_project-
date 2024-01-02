from .models import *
from rest_framework import serializers


class CategorySerilizar(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

class CustomerSerilizar(serializers.ModelSerializer):

    class Meta:
        model = Customer   
        fields = "__all__"

class ProductSerilizar(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['pro_id','pro_title','pro_price','pro_category','pro_rating']
        # exclude = ['pro_image']
class CartSerilizar(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = "__all__"


class OrderSerilizar(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = "__all__"        



class PersonSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    mobile_no = serializers.IntegerField()

