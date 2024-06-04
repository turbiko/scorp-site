import os
import logging
from datetime import datetime

from django.db import models
from django.utils.translation import activate, gettext_lazy as _, get_language
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator  # pagination

from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable, Locale
from wagtail.admin.panels import InlinePanel, PageChooserPanel, FieldPanel

logger = logging.getLogger('animagrad')


class NewsArticle(Page):
    template = 'ournews' + os.sep + 'news-page.html'

    news_date = models.DateField(verbose_name=_('news date'))
    short_text = RichTextField(blank=True, max_length=6500)
    big_text = RichTextField(blank=True, max_length=62000)
    big_picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('project top image')
    )
    slider_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('project image for slider')
    )

    content_panels = Page.content_panels + [
        FieldPanel('news_date'),
        FieldPanel('short_text'),
        FieldPanel('big_text'),
        FieldPanel('big_picture'),
        FieldPanel('slider_image'),
    ]

