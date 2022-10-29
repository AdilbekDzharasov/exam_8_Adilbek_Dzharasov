from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DeleteView
from webapp.models import Review


class ReviewDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'reviews/review_delete.html'
    model = Review
    context_object_name = 'review'
    permission_required = 'webapp.delete_review'

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.product.pk})

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

