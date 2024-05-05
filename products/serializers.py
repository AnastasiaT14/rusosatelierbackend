from rest_framework import serializers
from .models import Product, Category, ProductImageUrl


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductImageUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageUrl
        fields = ['image_url', 'alt']


class ProductEditSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = ProductImageUrl
        fields = ['id', 'image_url', 'alt']


class ProductCreateSerializer(serializers.ModelSerializer):
    image_urls = ProductImageUrlSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'image_urls']

    def create(self, validated_data):
        image_urls_data = validated_data.pop("image_urls")
        product = Product.objects.create(**validated_data)
        for image_url_data in image_urls_data:
            ProductImageUrl.objects.create(product=product, **image_url_data)
        return product


class ProductUpdateSerializer(serializers.ModelSerializer):
    image_urls = ProductEditSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'image_urls']

    def update(self, instance, validated_data):
        image_urls_data = validated_data.pop('image_urls', [])

        for field in ['name', 'description', 'category', 'price']:
            setattr(instance, field, validated_data.get(field, getattr(instance, field)))
        instance.save()

        existing_image_ids = [image['id'] for image in image_urls_data if 'id' in image]
        ProductImageUrl.objects.filter(product=instance).exclude(id__in=existing_image_ids).delete()

        for image_url_data in image_urls_data:
            image_id = image_url_data.get('id', None)
            image_url = image_url_data.get('image_url')

            if image_id:
                existing_image_url = ProductImageUrl.objects.get(id=image_id)
                existing_image_url.image_url = image_url
                existing_image_url.alt = image_url_data.get('alt')
                existing_image_url.save()

            if not image_id:
                ProductImageUrl.objects.create(product=instance, image_url=image_url, alt=image_url_data.get('alt', ''))

        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
