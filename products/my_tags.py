from django import template

from products.models import ProductModel

register = template.Library()

@register.simple_tag()
def heart_icon(request, product):
    if request.user in product.wishlist.all():
         return "fa-solid fa-heart"
    return "far fa-heart"


@register.simple_tag()
def cart_icon(request, product):
    if request.user in product.cart.all():
         return "fa-regular fa-trash-can"
    return "fas fa-cart-plus"


@register.simple_tag()
def is_in_cart(request, product):
    if request.user.is_authenticated:
        return product.cart.filter(id=request.user.id).exists()
    return False