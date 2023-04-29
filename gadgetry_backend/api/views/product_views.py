from rest_framework.generics import ListCreateAPIView , RetrieveAPIView, ListAPIView

from ..models import Product
from ..Serializers import ProductBrandSerializer, ProductReviewSerializer, ProductSerializer


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


class ListAllBrands(ListAPIView):
    queryset = Product.objects.all().distinct('productBrand')
    serializer_class = ProductBrandSerializer

listAllBrands = ListAllBrands.as_view()
retriveProduct = RetrieveProductView.as_view()
getAllProductsOrCreate = ListCreateProductView.as_view()