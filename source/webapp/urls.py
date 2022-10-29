from django.urls import path
from webapp.products_views.product_home import HomeProductView
from webapp.products_views.product_detail import ProductDetailView
from webapp.products_views.product_add import ProductCreateView
from webapp.products_views.products_update import ProductUpdateView
from webapp.products_views.product_delete import ProductDeleteView
from webapp.reviews_views.review_add import ProductReviewAddView
from webapp.reviews_views.review_update import ReviewUpdateView
from webapp.reviews_views.review_delete import ReviewDeleteView


urlpatterns = [
    path('', HomeProductView.as_view(), name='product_home'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/review/add/', ProductReviewAddView.as_view(), name='product_review_add'),
    path('reviews/update/<int:pk>', ReviewUpdateView.as_view(), name='review_update'),
    path('reviews/delete/<int:pk>', ReviewDeleteView.as_view(), name='review_delete')
]

