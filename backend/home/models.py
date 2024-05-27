import os
import logging
from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.contrib.settings.models import BaseSiteSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.models import Page, Orderable
from wagtail.admin.panels import InlinePanel, PageChooserPanel, FieldPanel
from wagtail.fields import RichTextField
from wagtail.documents import get_document_model

from core.settings import base as core_base

logger = logging.getLogger('lighttv')


class Contact(models.Model):
    name = models.CharField(max_length=230, verbose_name='Ім’я')
    email = models.EmailField(max_length=255, verbose_name='Електронна пошта')
    message = models.TextField(verbose_name='Повідомлення')

    def __str__(self):
        return f"Contact {self.name}"


class SocialMediaLink(Orderable):
    site_setting = ParentalKey('SocialMediaSettings', related_name='social_media_links')
    name = models.CharField(max_length=255, help_text='Назва соціальної мережі')
    logotype = models.FileField(max_length=255, help_text='Завантажте логотип соціальної мережі')
    url = models.URLField(help_text='URL посилання на соціальну мережу')

    panels = [
        FieldPanel('name'),
        FieldPanel('logotype'),
        FieldPanel('url'),
    ]

    def __str__(self):
        return f"Social: {self.name}"

    def get_svg_code(self):
        if not self.logotype:
            return ""

        svg_path = os.path.join(core_base.MEDIA_ROOT, self.logotype.name)
        try:
            with open(svg_path, 'r') as file:
                return file.read()
        except IOError:
            return ""


class ContactData(Orderable):
    site_setting = ParentalKey('ContactDataSettings', related_name='contact_data')
    phone = models.CharField(max_length=200, blank=True, null=True)
    post_addr = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)


@register_setting
class SocialMediaSettings(BaseSiteSetting, ClusterableModel):
    panels = [
        InlinePanel('social_media_links', label="Соціальні мережі"),
    ]
    class Meta:
        verbose_name = "Налаштування соціальних мереж"


@register_setting
class ContactDataSettings(BaseSiteSetting, ClusterableModel):
    panels = [
        InlinePanel('contact_data', label="Контактні дані", max_num=1),
    ]

    def get_contact_data(self):
        return self.contact_data.first()  # Повертаємо перший запис

    class Meta:
        verbose_name = "Налаштування контактних даних"


class HomePage(Page):
    about_name = models.CharField(_('Про нас назва блоку'), max_length=50, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('about_name'),

    ]

    def get_context(self, request):
        logger.info(f'Homepage (get_context) was accessed by {request.user} ')
        context = super().get_context(request)

        return context
