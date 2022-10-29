from django.urls import reverse
from django.views.generic import CreateView
from webapp.models import Product
from webapp.forms import ProductForm


class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/product_add.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_home')

