from django.urls import path

from blog.views import post_list_view, post_detail_view, post_like_view
from products import views
from products.views import HomeListView, ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    # Asosiy sahifalar
    path('', HomeListView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('shop/', ProductListView.as_view(), name='shop'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),

    # Wishlist (Xohishlar ro'yxati)
    path('wishlist/add/<int:pk>/', views.create_wishlist, name='wishlist_create'),
    path('wishlist/', views.wishlist_list, name='wishlist'),
    path('wishlist/delete/<int:pk>/', views.wishlist_delete, name='wishlist_delete'),
    path('wishlist/clear/', views.clear_wishlist, name='wishlist_clear'),

    # Cart (Savat)
    path('cart/', views.cart_list, name='cart'),
    path('cart/add/<int:pk>/', views.create_cart, name='create_cart'),  # 'create_cart' nomi shop.html dagi nomga moslandi
    path('cart/delete/<int:pk>/', views.cart_delete, name='cart-delete'),
    path('cart/plus/<int:pk>/', views.cart_plus, name='cart-plus'),
    path('cart/minus/<int:pk>/', views.cart_minus, name='cart-minus'),
    path('posts/', post_list_view, name='post-list'),
    path('posts/<slug:slug>/', post_detail_view, name='post-detail'),
    path('posts/<slug:slug>/like/', post_like_view, name='post-like')
]