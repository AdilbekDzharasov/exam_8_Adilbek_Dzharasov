from django import forms
from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'image')


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search")

