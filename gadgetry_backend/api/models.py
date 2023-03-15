import uuid
from django.db import models

# Create your models here.
# USER Class
class User(models.Model):
    userName = models.CharField(max_length=50,primary_key=True)
    userPassword = models.CharField(max_length=50)
    User = models.CharField(max_length=100)


class Product(models.Model):
    productName = models.CharField(max_length=100, primary_key=True)
    productBrand = models.CharField(max_length= 30)
    productDateAdded = models.DateField()
    productDimensions = models.CharField(max_length= 20)
    productImageUrl = models.TextField()
    Username = models.ForeignKey('User',on_delete=models.CASCADE)


class Review(models.Model):
    ReviewId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    productName = models.ForeignKey('Product',on_delete=models.CASCADE)
    username = models.ForeignKey('User',on_delete=models.CASCADE)
    reviewText = models.TextField()
    reviewDate = models.DateTimeField()
    reviewRating = models.IntegerField()