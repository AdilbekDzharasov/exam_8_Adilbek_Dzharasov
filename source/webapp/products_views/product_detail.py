from django.views.generic import DetailView
from webapp.models import Product


class ProductDetailView(DetailView):
    template_name = "products/product.html"
    context_object_name = 'product'
    model = Product

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tasks'] = self.object.tasks.order_by("-created_at")
    #     return context

