from django.http import Http404
from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, ProductCreateSerializer, ProductDetailsSerializer
from rest_framework import permissions


class ProductCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]#adminze
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class ProductList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdate(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class ProductDelete(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# category
class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdate(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDelete(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FilterProducts(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        category_name = self.kwargs['name']
        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            raise Http404("Category does not exist")
        queryset = Product.objects.filter(category=category)
        return queryset