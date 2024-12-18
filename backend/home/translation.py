from modeltranslation.translator import register, TranslationOptions
from .models import ContactData, ContactDataSettings, CareerTitles, OurTeam


@register(ContactData)
class ContactDataTranslationOptions(TranslationOptions):
    fields = ('name', 'phone', 'post_addr', 'post_addr2', 'email', 'email_requests', 'viber_contact', 'telegram_contact')


@register(ContactDataSettings)
class ContactDataSettingsTranslationOptions(TranslationOptions):
    fields = ()


@register(CareerTitles)
class CareerTitlesTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(OurTeam)
class OurTeamTranslationOptions(TranslationOptions):
    fields = ('position', 'name', 'last_name',)
