from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView
from webapp.models import Review
from webapp.forms import ProductReviewForm


class ReviewUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'reviews/review_update.html'
    form_class = ProductReviewForm
    model = Review
    context_object_name = 'review'
    permission_required = 'webapp.change_review'

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.product.pk})

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

