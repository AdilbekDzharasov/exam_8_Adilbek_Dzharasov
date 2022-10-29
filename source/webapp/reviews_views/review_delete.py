from django.urls import reverse
from django.views.generic import DeleteView
from webapp.models import Review


class ReviewDeleteView(DeleteView):
    template_name = 'reviews/review_delete.html'
    model = Review
    context_object_name = 'review'

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.product.pk})

