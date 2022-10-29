from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('other', 'Other'),
        ('sport', 'Sport'),
        ('computers', 'Computers')
    ]

    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Name"
    )
    category = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_CHOICES[0][0],
        verbose_name='Category'
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name="Description"
    )
    image = models.ImageField(
        upload_to="images",
        null=True,
        blank=True,
        verbose_name="image"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of creation'
    )
    changed_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date of change'
    )
    is_deleted = models.BooleanField(
        verbose_name='Is deleted',
        default=False,
        null=False
    )

    def __str__(self):
        return f"{self.name} - {self.category}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Review(models.Model):
    DEFAULT_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    author = models.ForeignKey(
        to=User,
        related_name='reviews',
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='Author'
    )
    product = models.ForeignKey(
        to="webapp.Product",
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Product"
    )
    review_text = models.TextField(
        max_length=5000,
        null=False,
        blank=False,
        verbose_name="Review text"
    )
    grade = models.IntegerField(
        null=False,
        blank=False,
        choices=DEFAULT_CHOICES,
        verbose_name="Grade"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of creation'
    )
    changed_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date of change'
    )
    is_deleted = models.BooleanField(
        verbose_name='Is deleted',
        default=False,
        null=False
    )

    def __str__(self):
        return f"{self.author}. {self.product}. {self.review_text}. {self.grade}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

