from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView
from webapp.models import Product
from webapp.forms import ProductForm
from webapp.products_views.group_permission import GroupPermission


class ProductCreateView(GroupPermission, LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'products/product_add.html'
    form_class = ProductForm
    groups = ['Moderators']

    def get_success_url(self):
        return reverse('product_home')

