from django.urls import path

from .views.user_management_views import getUser,createOrListuserView
from .views.product_views import getAllProductsOrCreate, retriveProduct
from .views.review_views import createReview , listReviewOnfilter

# Add DRF router later
urlpatterns = [
    path('ListCreateUser',createOrListuserView),
    path('getUser/<str:pk>',getUser),
    path('getProduct/<str:productName>',retriveProduct),
    path('ListCreateProduct/',getAllProductsOrCreate),
    path('createReview/',createReview),
    path('listReview/',listReviewOnfilter)
]