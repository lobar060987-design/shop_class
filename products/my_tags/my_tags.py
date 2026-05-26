from django import template


register = template.Library()

@register.simple_tag
def is_in_cart(request, product):
    return product in request.user.cart.products.all()



@register.simple_tag
def heart_icon(request, product):
    if product in request.user.wishlist.products.all():
        return "fas fa-heart"
    return "far fa-heart"


@register.simple_tag
def cart_icon(request, product):
    if product in request.user.cart.products.all():
        return "fas fa-shopping-cart"
    return "fas fa-cart-plus"

@register.simple_tag
def heart_icon(request, product):

    if request.user.is_authenticated:2

        if product.wishlist_set.filter(user=request.user).exists():
            return 'fas fa-heart'

    return 'far fa-heart'