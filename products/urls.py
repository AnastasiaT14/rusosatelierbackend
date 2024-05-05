from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('product_create/', views.ProductCreate.as_view(), name='product-create'),
    path('product_list/', views.ProductList.as_view(), name='product-list'),
    path('product_details/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('product_update/<int:pk>/', views.ProductUpdate.as_view(), name='product-update'),
    path('product_delete/<int:pk>/', views.ProductDelete.as_view(), name='product-delete'),
    # category
    path('category_list/', views.CategoryList.as_view(), name='category-list'),
    path('category_create/', views.CategoryCreate.as_view(), name='category-create'),
    path('category_detail/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('category_update/<int:pk>/', views.CategoryUpdate.as_view(), name='category-update'),
    path('category_delete/<int:pk>/', views.CategoryDelete.as_view(), name='category-delete'),
    path('admin123/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
