from django.contrib import admin
from .models import Category,Product,ProductImageUrl
from config.models import Feedback
# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImageUrl)
admin.site.register(Feedback)