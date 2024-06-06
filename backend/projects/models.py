import os
import logging
from datetime import datetime

from django.db import models
from django.utils.translation import activate, gettext_lazy as _, get_language
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator  # pagination

from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable, Locale
from wagtail.admin.panels import InlinePanel, PageChooserPanel, FieldPanel

from ournews.models import NewsArticle

logger = logging.getLogger('animagrad')


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

    def __str__(self):
        return self.title

    def get_context(self, request):  # Project
        context = super().get_context(request)
        # context['projects'] for carousel
        projects = Project.objects.live().filter(locale=Locale.get_active())
        logger.debug(f'Projects (get_context) for {request.user} {projects.count()=}')

        context['projects'] = projects
        return context


class Projects(Page):
    template = 'projects' + os.sep + 'projects-list.html'
    parent_page_types = ['home.HomePage']
    child_page_types = ['projects.Project']
    max_count_per_parent = 1
    # max_count = 1

    def get_context(self, request):  # Projects_List
        context = super().get_context(request)
        # Get projects accessible for user
        # all_projects = self.accessible(request=request)
        projects = Project.objects.live().filter(locale=Locale.get_active())
        logger.debug(f'Projects (get_context) for {request.user} {projects.count()=}')

        context['projects'] = projects
        return context


class NewsList(Page):
    template = 'projects' + os.sep + 'news-list.html'
    parent_page_types = ['home.HomePage']
    max_count_per_parent = 1

    posts_per_page = models.IntegerField(default=4)
    left_picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('left image')
    )
    right_picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('right image')
    )
    content_panels = Page.content_panels + [
        FieldPanel('posts_per_page'),
        FieldPanel('left_picture'),
        FieldPanel('right_picture'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)

        all_news = NewsArticle.objects.live().filter(locale=Locale.get_active())
        logger.debug(f'Projects (get_context) for {request.user} {all_news.count()=}')

        paginator = Paginator(all_news, self.posts_per_page)
        page = request.GET.get('page')

        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            news = paginator.page(1)
        except EmptyPage:
            news = paginator.page(paginator.num_pages)

        context['news'] = news
        return context
