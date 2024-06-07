import os
import logging
from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page, Orderable, Locale
from wagtail.admin.panels import InlinePanel, PageChooserPanel, FieldPanel
from wagtail.fields import RichTextField

logger = logging.getLogger(__name__)


class Service(Page):
    template = 'services' + os.sep + 'service.html'
    parent_page_types = [
        'services.ServiceProduction',
        'services.ServicePreProduction',
        'services.ServicePostProduction',
        'services.ServiceArtStoryProduction',
    ]


class ServiceProduction(Page):
    template = 'services' + os.sep + 'service-production.html'
    parent_page_types = ['services.ServicesList']
    child_page_types = ['services.Service']
    max_count_per_parent = 1

    body = RichTextField(_('Body'), blank=True, null=True)
    service_painting = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('service picture')
    )
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('service icon')
    )
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('service_painting'),
        FieldPanel('icon'),
    ]


class ServicePreProduction(Page):
    template = 'services' + os.sep + 'service-preproduction.html'
    parent_page_types = ['services.ServicesList']
    child_page_types = ['services.Service']
    max_count_per_parent = 1

    body = RichTextField(_('Body'), blank=True, null=True)
    service_painting = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('service picture')
    )
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('service icon')
    )
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('service_painting'),
        FieldPanel('icon'),
    ]


class ServicePostProduction(Page):
    template = 'services' + os.sep + 'service-postproduction.html'
    parent_page_types = ['services.ServicesList']
    child_page_types = ['services.Service']
    max_count_per_parent = 1

    body = RichTextField(_('Body'), blank=True, null=True)
    service_painting = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('service picture')
    )
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('service icon')
    )
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('service_painting'),
        FieldPanel('icon'),
    ]


class ServiceArtStoryProduction(Page):
    template = 'services' + os.sep + 'service-artstoryproduction.html'
    parent_page_types = ['services.ServicesList']
    child_page_types = ['services.Service']
    max_count_per_parent = 1

    body = RichTextField(_('Body'), blank=True, null=True)
    body2 = RichTextField(_('Body 2'), blank=True, null=True)
    service_painting = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('service picture')
    )
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('service icon')
    )
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('body2'),
        FieldPanel('service_painting'),
        FieldPanel('icon'),
    ]


class ServicesList(Page):
    template = 'services' + os.sep + 'services-list.html'
    parent_page_types = ['home.HomePage']
    child_page_types = ['services.ServiceType']
    max_count_per_parent = 1

    def get_context(self, request, *args, **kwargs):

        logger.info(f'ServicesList (get_context) was accessed by {request.user} ')
        context = super().get_context(request)
        all_services = self.get_children().live().filter(locale=Locale.get_active())
        logger.debug(f'Projects (get_context) for {request.user} {all_services.count()=}')

        context['all_services'] = all_services

        return context
