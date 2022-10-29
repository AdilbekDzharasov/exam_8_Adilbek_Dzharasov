from django.urls import path
from webapp.products_views.product_home import HomeProductView
from webapp.products_views.product_detail import ProductDetailView
from webapp.products_views.product_add import ProductCreateView
from webapp.products_views.products_update import ProductUpdateView
from webapp.products_views.product_delete import ProductDeleteView


urlpatterns = [
    path('', HomeProductView.as_view(), name='product_home'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('projects/delete/<int:pk>', ProductDeleteView.as_view(), name='project_delete')
]

