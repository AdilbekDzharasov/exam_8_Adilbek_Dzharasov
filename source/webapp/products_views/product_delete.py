from django.urls import reverse_lazy
from django.views.generic import DeleteView
from webapp.models import Product


class ProductDeleteView(DeleteView):
    template_name = 'products/product_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('product_home')

