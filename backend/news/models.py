import os
import logging
from datetime import datetime

from django.db import models
from django.utils.translation import activate, gettext_lazy as _, get_language
from wagtail.fields import RichTextField

from wagtail.models import Page, Orderable, Locale
from wagtail.admin.panels import InlinePanel, PageChooserPanel, FieldPanel

logger = logging.getLogger('mavka')

class NewsArticle(Page):
    template = 'news' + os.sep + 'news-article.html'
    parent_page_types = ['projects.Project', 'news.NewsList']
    child_page_types = []

    short_text = models.TextField(blank=True)
    big_text = RichTextField(blank=True)
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
        FieldPanel('big_picture'),
        FieldPanel('slider_image'),
    ]


class NewsList(Page):
    template = 'news' + os.sep + 'news-article.html'
    parent_page_types = ['home.HomePage']
    child_page_types = ['news.NewsArticle']
    max_count = 1

    def get_context(self, request):  # Projects_List
        context = super().get_context(request)
        # Get projects accessible for user
        # all_projects = self.accessible(request=request)
        news = NewsArticle.objects.live().filter(locale=Locale.get_active())
        logger.debug(f'NewsList (get_context) for {request.user} {news.count()=}')

        context['news'] = news
        return context
