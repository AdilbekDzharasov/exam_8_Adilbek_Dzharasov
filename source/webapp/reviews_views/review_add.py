from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView
from webapp.models import Review
from webapp.forms import ProductReviewForm
from webapp.models import Product


class ProductReviewAddView(CreateView):
    model = Review
    template_name = 'reviews/product_review_add.html'
    form_class = ProductReviewForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        review = form.save(commit=False)
        review.product = product
        review.save()
        return redirect('product_detail', pk=product.pk)

