from .models import *
from rest_framework.views import APIView
from .serializars import *
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# =========================Simple form Query ==============
# get getwithid post update delete
# without id  - get, post
# with id     - getwithid, update, delete
# ================================================

class CategoryListCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizar

class CategoryUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizar   



class CustomerListCreate(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerilizar

class CategoryUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerilizar  



class ProductListCreate(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizar

class ProductUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizar  



class CartListCreate(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerilizar

class CartUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerilizar  



class OrderListCreate(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerilizar

class OrderUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerilizar  



# =============================================

class PersonAPI(APIView):
    def post(self, request):   
        serializer = PersonSerializer(data = request.POST)  # serialization
        if serializer.is_valid():
            first_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']
            mobile_no = serializer.validated_data['mobile_no']

            print(first_name, last_name, mobile_no)
            return Response({'first_name':first_name},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 




















# ============================= CategoryAPI ==================================================

# class CategoryAPI(APIView):
#     def get(self, request, pk=None):   
#         if pk == None:
#             cat_data = Category.objects.all()   # djnago orm (complex data)    
#             serializer = CategorySerilizar(cat_data,many=True )  # serialization
#             return Response(serializer.data)
#         else:
#             cat_data = Category.objects.get(id = pk)   # djnago orm (complex data)    
#             serializer = CategorySerilizar(cat_data )
#             return Response(serializer.data)


#     def post(self, request):
#         serializer = CategorySerilizar(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'data created successfullty'},status=status.HTTP_201_CREATED) 
#         else:
#              return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  



#     def put(self, request,pk = None):
#         cat_data = Category.objects.get(id = pk)
#         serializer = CategorySerilizar(cat_data,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": 'data updated successfullty'},status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
#     def patch(self, request,pk = None):
#         cat_data = Category.objects.get(id = pk)
#         serializer = CategorySerilizar(cat_data,data = request.data,partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": 'data updated successfullty'},status=status.HTTP_202_ACCEPTED)
#         else:
#            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
#     def delete(self, request, pk = None):
#         cat_data = Category.objects.get(id = pk)
#         cat_data.delete()
#         return Response({"msg": 'data Deleted successfullty'},status=status.HTTP_202_ACCEPTED)
    
# # ================= Product API =======================================================
# class ProductAPI(APIView):
#     def get(self,request,pk=None):
#         if pk == None:
#             pro_data = Product.objects.all()
#             serializer = ProductSerilizar(pro_data,many=True)
#             return Response(serializer.data)
#         else:
#             pro_data = Product.objects.get(id = pk)
#             serializer = ProductSerilizar(pro_data)
#             return Response(serializer.data)
        

#     def post(self, request):
#         serializer = ProductSerilizar(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'data created successfullty'},status=status.HTTP_201_CREATED) 
#         else:
#              return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 


#     def put(self, request,pk = None):
#         pro_data = Product.objects.get(id = pk)
#         serializer = ProductSerilizar(pro_data,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": 'data updated successfullty'},status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request,pk = None):
#         pro_data = Product.objects.get(id = pk)
#         serializer = ProductSerilizar(pro_data,data = request.data,partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": 'data updated successfullty'},status=status.HTTP_202_ACCEPTED)
#         else:
#            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        


#     def delete(self, request, pk = None):
#         cat_data = Product.objects.get(id = pk)
#         cat_data.delete()
#         return Response({"msg": 'data Deleted successfullty'},status=status.HTTP_202_ACCEPTED)
    

# =======================================================================================================





