from modeltranslation.translator import register, TranslationOptions

from products.models import CategoryModel, ProductModel, ColorModel


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = 'name',


@register(ColorModel)
class ColorTranslationOptions(TranslationOptions):
    fields = 'name',


@register(ProductModel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description', 'long_description',)


