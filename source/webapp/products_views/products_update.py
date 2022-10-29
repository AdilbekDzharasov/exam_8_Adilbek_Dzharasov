from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView
from webapp.forms import ProductForm
from webapp.models import Product
from webapp.products_views.group_permission import GroupPermission


class ProductUpdateView(GroupPermission, LoginRequiredMixin, UpdateView):
    template_name = 'products/product_update.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'
    groups = ['Moderators']

    def get_success_url(self):
        return reverse('product_home')

