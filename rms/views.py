from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category,Table,OrderItem
from .serializer import CategorySerializer,TableSerializer

# Create your views here.
# class based : API view
from rest_framework.views import APIView

class CategoryAPIView(APIView):
    def get(self,request):
        category=Category.objects.all()
        serializer=CategorySerializer(category,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class CategoryDetail(APIView):
    def get(self,request,id):
        category=Category.objects.get(id=id)        
        serializer=CategorySerializer(category)
        return Response(serializer.data)
    
    def post(self,request,id):
        category=Category.objects.get(id=id) 
        serializer=CategorySerializer(category,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data) 
    
    def delete(self,request,id):
        category=Category.objects.get(id=id) 
        items=OrderItem.objects.filter(food__category=category).count()
        if items>0:
            return Response({"details":"Catetgory Cannont be deleted"})
            category.delete()
        return Response('Category Deleted Successfully')
            



# Fuinction based : api_view()
# @api_view(['GET','POST'])
# def category(request):
#     if request.method=="GET":
#         category=Category.objects.all()
#         serializer=CategorySerializer(category,many=True)
#         return Response(serializer.data)
#     elif request.method=="POST":
#         serializer=CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data) 
    
# @api_view(['GET','POST','DELETE'])
# def category_detail(request,id):
#     category=Category.objects.get(id=id)
#     if request.method=="GET":
#         serializer=CategorySerializer(category)
#         return Response(serializer.data)
#     elif request.method=="POST":
#         serializer=CategorySerializer(category,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data) 
#     elif request.method=='DELETE':
#         items=OrderItem.objects.filter(food__category=category).count()
#         if items>0:
#             return Response({"details":"Catetgory Cannont be deleted"})
#         category.delete()
#         return Response('Category Deleted Successfully')
    
        


# @api_view()
# def table(request):
#     table=Table.objects.all()
#     serializer=TableSerializer(table,many=True)
#     return Response(serializer.data)

