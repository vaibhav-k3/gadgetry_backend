from django.urls import path

from .views.user_management_views import getUser,createOrListuserView, verifyUser
from .views.product_views import getAllProductsOrCreate, retriveProduct
from .views.review_views import createReview , listReviewOnfilter
from .views.chart_views import brand_chart_view
# Add DRF router later
urlpatterns = [
    path('ListCreateUser',createOrListuserView),
    path('getUser/<str:pk>',getUser),
    path('getProduct/<str:productName>',retriveProduct),
    path('ListCreateProduct/',getAllProductsOrCreate),
    path('createReview/',createReview),
    path('listReview/',listReviewOnfilter),
    path('verifyUser/',verifyUser),
    path('brandchart/',brand_chart_view)
]