import os
import logging
from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page, Orderable
from wagtail.admin.panels import InlinePanel, PageChooserPanel, FieldPanel

logger = logging.getLogger('mavka')


class ServiceType(Page):
    template = 'services' + os.sep + 'service-type.html'
    parent_page_types = ['services.ServicesList']


class ServicesList(Page):
    template = 'services' + os.sep + 'services-list.html'
    parent_page_types = ['home.HomePage']
    child_page_types = ['services.ServiceType']
    max_count_per_parent = 1
