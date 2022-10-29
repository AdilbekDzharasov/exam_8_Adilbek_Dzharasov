from django.urls import reverse
from django.views.generic import UpdateView
from webapp.models import Review
from webapp.forms import ProductReviewForm


class ReviewUpdateView(UpdateView):
    template_name = 'reviews/review_update.html'
    form_class = ProductReviewForm
    model = Review
    context_object_name = 'review'

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.product.pk})

