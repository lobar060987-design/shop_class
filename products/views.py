from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView
from blog.models import BannerModel, PostModel  # PostModel'ni shu yerga chiroyli qo'shdik
from products.models import CategoryModel, ProductModel, BrandModel, ColorModel, SizeModel, CartModel


# --- Class Based Views (Sahifalar uchun klasslar) ---

class AboutView(TemplateView):
    template_name = 'about.html'


class HomeListView(ListView):
    template_name = 'index.html'
    queryset = ProductModel.objects.order_by('-pk')[:3]
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.order_by('-pk')[:3]
        context['banner'] = BannerModel.objects.order_by('-pk').first()

        # MANA SHU YERGA POSTLARNI QO'SHTIK AKA!
        # Endi index.html sahifasida blog postlar muammosiz ko'rinadi
        context['posts'] = PostModel.objects.order_by('-pk')[:3]
        return context


class ProductListView(ListView):
    template_name = 'shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        qs = ProductModel.objects.order_by('-pk')
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__icontains=q)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['colors'] = ColorModel.objects.all()
        context['sizes'] = SizeModel.objects.all()
        return context


class ProductDetailView(DetailView):
    template_name = 'shop-single.html'
    model = ProductModel
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = self.get_object().category.products.order_by('-pk').exclude(
            pk=self.get_object().pk
        )[:10]
        return context


# --- Wishlist (Xohishlar ro'yxati logikasi) ---

@login_required
def create_wishlist(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    if request.user in product.wishlist.all():
        product.wishlist.remove(request.user)
    else:
        product.wishlist.add(request.user)
    product.save()
    return redirect(request.GET.get('next', '/'))


@login_required
def wishlist_list(request):
    products = request.user.wishlist.all()
    context = {'products': products}
    return render(request, 'wishlist.html', context)


@login_required
def wishlist_delete(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    product.wishlist.remove(request.user)
    return redirect(request.GET.get('next', '/'))


@login_required
def clear_wishlist(request):
    request.user.wishlist.clear()
    return redirect('products:wishlist')


# --- Cart (Savat logikasi) ---

@login_required
def create_cart(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)

    cart_item, created = CartModel.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.GET.get('next', '/'))


@login_required
def cart_list(request):
    products = CartModel.objects.filter(user=request.user)

    total = 0

    for item in products:
        total += item.get_total_price()

    context = {
        'products': products,
        'total': total
    }

    return render(request, 'cart.html', context)


@login_required
def cart_plus(request, pk):
    cart_item = get_object_or_404(
        CartModel,
        user=request.user,
        product_id=pk
    )

    cart_item.quantity += 1
    cart_item.save()

    return redirect('products:cart')


@login_required
def cart_minus(request, pk):
    cart_item = get_object_or_404(
        CartModel,
        user=request.user,
        product_id=pk
    )

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('products:cart')


@login_required
def cart_delete(request, pk):
    cart_item = get_object_or_404(
        CartModel,
        user=request.user,
        product_id=pk
    )

    cart_item.delete()

    return redirect('products:cart')