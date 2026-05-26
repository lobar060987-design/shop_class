from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# 1. Til prefiksi shart bo'lmagan URL-lar (Masalan: i18n o'zi)
urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

# 2. Til prefiksi (en/, ru/) bilan ochilishi kerak bo'lgan URL-lar
urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path(
        "", include("products.urls")
    ),  # Bosh sahifa va mahsulotlar (en/ yoki en/shop/)
    path("users/", include("users.urls")),
    path("blog/", include("blog.urls")),
    path("contacts/", include("contacts.urls")),
    # Takrorlangan (dublikat) yo'llar olib tashlandi
)

# 3. Media va Static fayllar uchun sozlama (Faqat DEBUG=True bo'lganda)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)