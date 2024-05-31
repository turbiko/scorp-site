import os
import logging
from datetime import datetime

from django.db import models
from django.utils.translation import activate, gettext_lazy as _, get_language
from wagtail.fields import RichTextField

from wagtail.models import Page, Orderable, Locale
from wagtail.admin.panels import InlinePanel, PageChooserPanel, FieldPanel

logger = logging.getLogger('mavka')

class Project(Page):
    template = 'projects' + os.sep + 'project-page.html'
    parent_page_types = ['projects.Projects']

    category = models.TextField(blank=True, max_length=100)
    genre = models.TextField(blank=True, max_length=100)
    audience = models.TextField(blank=True, max_length=100)
    running_time = models.TextField(blank=True, max_length=100)
    format = models.TextField(blank=True, max_length=100)
    technique = models.TextField(blank=True, max_length=100)
    sound = models.TextField(blank=True, max_length=100)
    languages = models.TextField(blank=True, max_length=100)
    producers = models.TextField(blank=True, max_length=100)
    director = models.TextField(blank=True, max_length=100)
    screenplay = models.TextField(blank=True, max_length=100)
    short_text = models.TextField(blank=True, max_length=6500)
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
        FieldPanel('category'),
        FieldPanel('genre'),
        FieldPanel('running_time'),
        FieldPanel('audience'),
        FieldPanel('format'),
        FieldPanel('technique'),
        FieldPanel('sound'),
        FieldPanel('languages'),
        FieldPanel('producers'),
        FieldPanel('director'),
        FieldPanel('screenplay'),
        FieldPanel('short_text'),
        FieldPanel('big_text'),
        FieldPanel('big_picture'),
        FieldPanel('slider_image'),
    ]


class Projects(Page):
    template = 'projects' + os.sep + 'projects-list.html'
    parent_page_types = ['home.HomePage']
    child_page_types = ['projects.Project']
    max_count = 1
    def get_context(self, request):  # Projects_List
        context = super().get_context(request)
        # Get projects accessible for user
        # all_projects = self.accessible(request=request)
        projects = Project.objects.live().filter(locale=Locale.get_active())
        logger.debug(f'Projects (get_context) for {request.user} {projects.count()=}')

        context['projects'] = projects
        return context

