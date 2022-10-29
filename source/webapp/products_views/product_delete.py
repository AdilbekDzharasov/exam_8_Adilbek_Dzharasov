from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from webapp.models import Product
from webapp.products_views.group_permission import GroupPermission


class ProductDeleteView(GroupPermission, LoginRequiredMixin, DeleteView):
    template_name = 'products/product_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('product_home')
    groups = ['Moderators']

