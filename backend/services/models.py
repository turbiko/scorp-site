import os
import logging
from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page, Orderable
from wagtail.admin.panels import InlinePanel, PageChooserPanel, FieldPanel

logger = logging.getLogger('mavka')


class Service(Page):
    template = 'services' + os.sep + 'service.html'
    parent_page_types = [
        'services.ServiceProduction',
        'services.ServicePreProduction',
        'services.ServicePostProduction',
        'services.ServiceArtStoryProduction',
    ]
    # child_page_types = ['services.Service']


class ServiceProduction(Page):
    template = 'services' + os.sep + 'service-production.html'
    parent_page_types = ['services.ServicesList']
    child_page_types = ['services.Service']

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
        FieldPanel('service_painting'),
        FieldPanel('icon'),
    ]


class ServicePreProduction(Page):
    template = 'services' + os.sep + 'service-preproduction.html'
    parent_page_types = ['services.ServicesList']
    child_page_types = ['services.Service']

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
        FieldPanel('service_painting'),
        FieldPanel('icon'),
    ]


class ServicePostProduction(Page):
    template = 'services' + os.sep + 'service-postproduction.html'
    parent_page_types = ['services.ServicesList']
    child_page_types = ['services.Service']

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
        FieldPanel('service_painting'),
        FieldPanel('icon'),
    ]


class ServiceArtStoryProduction(Page):
    template = 'services' + os.sep + 'service-artstoryproduction.html'
    parent_page_types = ['services.ServicesList']
    child_page_types = ['services.Service']

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
        FieldPanel('service_painting'),
        FieldPanel('icon'),
    ]


class ServicesList(Page):
    template = 'services' + os.sep + 'services-list.html'
    parent_page_types = ['home.HomePage']
    child_page_types = ['services.ServiceType']
    max_count_per_parent = 1
