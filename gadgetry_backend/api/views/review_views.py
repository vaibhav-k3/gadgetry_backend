from rest_framework.generics import CreateAPIView, ListAPIView , DestroyAPIView, UpdateAPIView

from ..Serializers import ReviewSerializer
from ..models import Review

class CreateReviewView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ListReviewView(ListAPIView):
    """
    Filter reviews based on Ratings
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        minRating = int(self.request.query_params.get('minRating','0'))
        maxRating = int(self.request.query_params.get('maxRating','5'))
        return Review.objects.filter(reviewRating__gte = minRating, reviewRating__lte = maxRating )

class DeleteReviewView(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'ReviewId'

class UpdateReviewView(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'ReviewId'


updateReview = UpdateReviewView.as_view()
deleteReview = DeleteReviewView.as_view()
createReview = CreateReviewView.as_view()
listReviewOnfilter = ListReviewView.as_view()
