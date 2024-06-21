from modeltranslation.translator import TranslationOptions, register
from .models import Genre

@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name')

