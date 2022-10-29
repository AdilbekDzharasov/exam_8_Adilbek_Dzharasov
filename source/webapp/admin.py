from django.contrib import admin
from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'description', 'image', 'is_deleted']
    list_filter = ['id', 'name', 'category', 'description', 'image', 'is_deleted']
    search_fields = ['id', 'name', 'category', 'description']
    fields = ['name', 'category', 'description', 'image', 'is_deleted']
    readonly_fields = ['id']


admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'product', 'review_text', 'grade', 'is_deleted']
    list_filter = ['id', 'author', 'product', 'review_text', 'grade', 'is_deleted']
    search_fields = ['id', 'author', 'product']
    fields = ['author', 'product', 'review_text', 'grade', 'is_deleted']
    readonly_fields = ['id']


admin.site.register(Review, ReviewAdmin)

