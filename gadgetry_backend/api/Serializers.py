from rest_framework import serializers

from .models import User , Product , Review
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'

class ProductReviewSerializer(serializers.ModelSerializer):
    
    product_reviews = ReviewSerializer(many = True,read_only=True)
    class Meta:
        model = Product
        fields = '__all__'