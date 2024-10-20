import os
import logging
import uuid
from datetime import datetime

# from wagtail_localize.models import TranslatableMixin

from django.db import models
from django.utils.translation import activate, gettext_lazy as _, get_language
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator  # pagination

from modelcluster.fields import ParentalKey

from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable, Locale, TranslatableMixin
from wagtail.admin.panels import InlinePanel, PageChooserPanel, FieldPanel
from wagtail.snippets.models import register_snippet

from ournews.models import NewsArticle


logger = logging.getLogger(__name__)


@register_snippet
class Genre(TranslatableMixin, models.Model):
    translation_key = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class ProjectGenres(Orderable):
    page = ParentalKey('projects.Project', related_name='project_genres')
    genre = models.ForeignKey('projects.Genre', related_name='+', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.page.title} - {self.genre.name}"

    panels = [
        FieldPanel('genre'),
    ]


class Project(Page):
    template = 'projects' + os.sep + 'project-page.html'
    parent_page_types = ['projects.Projects']

    category = models.TextField(_('category'), blank=True, max_length=100)
    genre = models.TextField(_('genre'), blank=True, max_length=100)
    genres = models.ManyToManyField('projects.Genre', blank=True, verbose_name=_('genres'))
    audience = models.TextField(_('audience'), blank=True, max_length=100)
    running_time = models.TextField(_('running time'), blank=True, max_length=100)
    format = models.TextField(_('format'), blank=True, max_length=100)
    technique = models.TextField(_('technique'), blank=True, max_length=100)
    sound = models.TextField(_('sound'), blank=True, max_length=100)
    languages = models.TextField(_('Languages'), blank=True, max_length=100)
    producers = models.TextField(_('producers'), blank=True, max_length=100)
    director = models.TextField(_('director'), blank=True, max_length=100)
    screenplay = models.TextField(_('screenplay'), blank=True, max_length=100)
    short_text = models.TextField(_('short text'), blank=True, max_length=6500)
    big_text = RichTextField(_('big text'), blank=True, max_length=62000)
    big_picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('project top image'),
        help_text=_('project top image')
    )
    slider_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('project image for slider'),
        help_text=_('project image for slider')
    )
    content_panels = Page.content_panels + [
        FieldPanel('category', heading=_('Category')),
        # FieldPanel('genre'),
        # FieldPanel('genres'),  # try translations
        InlinePanel('project_genres', label=_("Project Genres")),
        FieldPanel('running_time', heading=_('Running Time')),
        FieldPanel('audience', heading=_('Audience')),
        FieldPanel('format', heading=_('Format')),
        FieldPanel('technique', heading=_('Technique')),
        FieldPanel('sound', heading=_('Sound')),
        FieldPanel('languages', heading=_('Languages')),
        FieldPanel('producers', heading=_('Producers')),
        FieldPanel('director', heading=_('Director')),
        FieldPanel('screenplay', heading=_('Screenplay')),
        FieldPanel('short_text', heading=_('Short Description')),
        FieldPanel('big_text', heading=_('Detailed Description')),
        FieldPanel('big_picture', heading=_('Main Image')),
        FieldPanel('slider_image', heading=_('Slider Image')),
    ]

    def __str__(self):
        return self.title

    def get_context(self, request):  # Project
        context = super().get_context(request)
        # context['projects'] for carousel
        projects = Project.objects.live().filter(locale=Locale.get_active())
        logger.debug(f'Projects (get_context) for {request.user} {projects.count()=}')
        context['projects'] = projects

        # Add genres to the context
        project_genres = self.project_genres.all()
        genres = [pg.genre for pg in project_genres if pg.genre]
        context['genres'] = genres

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
