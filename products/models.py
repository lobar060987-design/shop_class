from django.db import models

from users.models import UserModel


class CategoryModel(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class BrandModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class ColorModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"


class SizeModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"


class ProductModel(models.Model):
    name = models.CharField(max_length=100)

    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name='products',
    )

    brand = models.ForeignKey(
        BrandModel,
        on_delete=models.CASCADE,
        related_name='products'
    )

    colors = models.ManyToManyField(
        ColorModel,
        related_name='products',
        blank=True,
    )

    sizes = models.ManyToManyField(
        SizeModel,
        related_name='products',
        blank=True,
    )

    image = models.ImageField(
        upload_to='product_images/',
        null=True,
        blank=True
    )

    short_description = models.CharField(max_length=100)

    long_description = models.TextField()

    price = models.FloatField()

    discount = models.IntegerField(default=0)

    wishlist = models.ManyToManyField(
        UserModel,
        related_name='wishlist',
        blank=True,
    )

    # cart = models.ManyToManyField(
    #     UserModel,
    #     related_name='cart',
    #     blank=True,
    # )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def get_price(self):
        if self.discount != 0:
            return self.price - self.price / 100 * self.discount

        return self.price

    def is_discount(self):
        return True if self.discount else False


class BannerModel(models.Model):
    title = models.CharField(max_length=100)

    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.title


class CartModel(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='cart_items'
    )

    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='cart_items'
    )

    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product.get_price() * self.quantity

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"