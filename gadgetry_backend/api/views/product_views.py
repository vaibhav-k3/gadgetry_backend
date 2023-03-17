from rest_framework.generics import ListCreateAPIView , RetrieveAPIView

from ..models import Product
from ..Serializers import ProductReviewSerializer, ProductSerializer


## Refactor later
class ListCreateProductView(ListCreateAPIView):
    queryset  = Product.objects.all()
    serializer_class = ProductSerializer

class RetrieveProductView(RetrieveAPIView):
    """
    Get Product with all its review.
    """
    queryset  = Product.objects.all()
    serializer_class = ProductReviewSerializer
    lookup_field = 'productName'

# class RetriveProductwithReviews()
#     querset = Product.objects.all()
#     seri


retriveProduct = RetrieveProductView.as_view()
getAllProductsOrCreate = ListCreateProductView.as_view()