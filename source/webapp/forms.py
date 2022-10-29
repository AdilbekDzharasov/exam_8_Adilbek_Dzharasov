from django import forms
from django.forms import widgets
from webapp.models import Product
from webapp.models import Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'image')


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search")


class ProductReviewForm(forms.ModelForm):
    DEFAULT_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    grade = forms.ChoiceField(required=True, label='Grade', choices=DEFAULT_CHOICES)

    class Meta:
        model = Review
        fields = ('review_text', 'grade')


# class ReviewForm(forms.ModelForm):
#
#     class Meta:
#         model = Product
#         fields = ('review_text', 'grade')

