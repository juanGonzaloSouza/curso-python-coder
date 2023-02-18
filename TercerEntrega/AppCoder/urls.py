from django.urls import path
from .views import create_user, create_product, create_review, product_list, user_list, review_list

urlpatterns = [
    path('users/', create_user, name='create_user'),
    path('products/', create_product, name='create_product'),
    path('reviews/', create_review, name='create_review'),
    path('products/list/', product_list, name='product_list'),
    path('users/list/', user_list, name='user_list'),
    path('reviews/list/', review_list, name='review_list'),


]