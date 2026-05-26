from django.contrib import admin
from products.models import ColorModel, CategoryModel, ProductModel,SizeModel,BrandModel

from modeltranslation.admin import TranslationAdmin

class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(SizeModel)



@admin.register(ColorModel)
class ColorModelAdmin(MyTranslationAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(CategoryModel)
class CategoryModelAdmin(MyTranslationAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(ProductModel)
class ProductModelAdmin(MyTranslationAdmin):
    list_display = ['name','brand','category','get_price']
    search_fields = ['name','brand','category',]
    list_filter = ['name', 'brand', 'category', 'colors']

admin.site.register(BrandModel)