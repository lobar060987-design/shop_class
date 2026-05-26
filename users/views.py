from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# LoginForm ni ham import qilib olamiz
from users.forms import RegistrationForm, LoginForm, UserUpdateForm


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # UserCreationForm o'zi parolni ichida shifrlab saqlaydi
            user = form.save()
            login(request, user)
            messages.success(request, "Muvaffaqiyatli ro'yxatdan o'tdingiz!")
            return redirect('products:home')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        # formaga request va POST ma'lumotlarini beramiz
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            # AuthenticationForm o'zi foydalanuvchini tekshirib (authenticate qilib) beradi
            user = form.get_user()
            login(request, user)
            return redirect('products:home')
        else:
            messages.error(request, 'Username yoki password xato')
    else:
        form = LoginForm()

    # Formani ham render qilish uchun context'ga qo'shamiz
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Profil ma'lumotlari yangilandi!")
            return redirect('users:profile')
    else:
        form = UserUpdateForm(instance=request.user)

    wishlist_products = request.user.wishlist.all()
    cart_products = request.user.cart_items.all()

    context = {
        'form': form,
        'wishlist_products': wishlist_products,
        'cart_products': cart_products,
    }
    return render(request, 'profile.html', context)