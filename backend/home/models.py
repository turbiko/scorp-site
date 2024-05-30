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
from wagtail.admin.panels import MultiFieldPanel,  TabbedInterface, ObjectList
from wagtail.admin.panels import InlinePanel, PageChooserPanel, FieldPanel
from wagtail.fields import RichTextField
from wagtail.documents import get_document_model
from wagtail.api import APIField

from core.settings import base as core_base


logger = logging.getLogger('mavka')


class Contact(models.Model):  # contact form
    name = models.CharField(max_length=230, verbose_name=_('Name'))
    email = models.EmailField(max_length=255, verbose_name=_('Email address'))
    message = models.TextField(verbose_name=_('Message'))

    def __str__(self):
        return f"Contact {self.name}"


class SocialMediaLink(Orderable):
    site_setting = ParentalKey('SocialMediaSettings', related_name='social_media_links')
    name = models.CharField(max_length=255, help_text=_('Social net name'))
    logotype = models.FileField(max_length=255, help_text=_('Upload logotype'))
    url = models.URLField(help_text=_('URL to social network account'))

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


class ContactData(Orderable):  # for site contact block
    site_setting = ParentalKey('ContactDataSettings', related_name='contact_data')
    phone = models.CharField(max_length=200, blank=True, null=True)
    post_addr = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)


@register_setting
class SocialMediaSettings(BaseSiteSetting, ClusterableModel):
    panels = [
        InlinePanel('social_media_links', label="Social networks"),
    ]

    class Meta:
        verbose_name = _("Social site settings")


@register_setting
class ContactDataSettings(BaseSiteSetting, ClusterableModel):  # for site contact block
    panels = [
        InlinePanel('contact_data', label=_("Contact data"), max_num=1),
    ]

    def get_contact_data(self):
        return self.contact_data.first()  # return only first element

    class Meta:
        verbose_name = _("Contact settings")


class PartnersLogotypes(Orderable):
    page = ParentalKey('wagtailcore.Page', related_name='partner_logo')
    name = models.CharField(max_length=150, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    logotype = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Partner name, URL and logotype')
    )


class HomePage(Page):
    max_count_per_parent = 1
    parent_page_types = ['wagtailcore.Page']
    child_page_types = ['services.ServicesList']

    big_picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Intro top image')
    )
    about_name = models.CharField(_('Name for about block'), max_length=50, blank=True, null=True)
    about_text = RichTextField(_('About'))
    about_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Intro top image')
    )
    block3_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('empty block background')
    )
    projects_title = models.CharField(_('Name for projects block'), max_length=50, blank=True, null=True)
    partners_title = models.CharField(_('Name for partners block'), max_length=50, blank=True, null=True)
    partners_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Partnets block background')
    )
    services_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('our services block background')
    )

    content_panels = Page.content_panels + [
        FieldPanel('big_picture'),
        FieldPanel('about_name'),
        FieldPanel('about_background'),
        FieldPanel('block3_background'),
        FieldPanel('projects_title'),
        FieldPanel('partners_title'),
        FieldPanel('partners_background'),
        InlinePanel('partner_logo', label=_("Partners logotypes")),
        FieldPanel('services_background'),
    ]

    def get_context(self, request):
        logger.info(f'Homepage (get_context) was accessed by {request.user} ')
        context = super().get_context(request)

        return context


class OurTeam(models.Model):
    position = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    big_picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Intro top image')
    )

    def __str__(self):
        return f"{self.name} {self.position}"


class OurTeamCompany(Orderable):
    our_team = models.ForeignKey(OurTeam, related_name='+', null=True, on_delete=models.SET_NULL)
    page = ParentalKey('home.About', related_name='our_team')


class About(Page):
    template = 'home' + os.sep + 'about.html'
    parent_page_types = ['home.HomePage']
    max_count = 1
    big_picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Intro top image')
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('big_picture'),
        ],
            heading=_("About Options"),
        ),
        MultiFieldPanel(
            [InlinePanel("our_team", label=_("Our team"))],
            heading=_("Team members"),
        ),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        team_members = self.our_team.all()

        grouped_teams = list(team_members)

        context['grouped_team_members'] = [grouped_teams[i:i + 2] for i in range(0, len(grouped_teams), 2)]

        return context

class ContactPage(Page):
    template = 'home' + os.sep + 'contactus.html'
    parent_page_types = ['home.HomePage']
    max_count = 1


class Career(Page):
    template = 'home' + os.sep + 'career.html'
    parent_page_types = ['home.HomePage']
    max_count = 1

class Services(Page):
    template = 'home' + os.sep + 'services.html'
    parent_page_types = ['home.HomePage']
    max_count = 1