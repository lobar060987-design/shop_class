from django.contrib import admin
from blog.models import BannerModel, PostModel


admin.site.register(BannerModel)
admin.site.register(PostModel)