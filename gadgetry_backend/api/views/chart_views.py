from rest_framework.generics import ListAPIView
from ..Serializers import BrandRatingSerializer
from ..models import Product , Review
from django.db.models import Count

class ChartBrandRatingView(ListAPIView):

    serializer_class = BrandRatingSerializer
    def get_queryset(self):
        requestedBrand = self.request.GET.get('brand')
        queryset = Review.objects.filter(productName__productBrand = requestedBrand).\
                  values('reviewRating').annotate(review_count =Count('ReviewId',distinct=True))
        
        return queryset

brand_chart_view = ChartBrandRatingView.as_view()