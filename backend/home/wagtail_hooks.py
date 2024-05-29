from wagtail_modeladmin.options import ModelAdmin, modeladmin_register

from .models import OurTeam, Contact


class OurTeamAdmin(ModelAdmin):
    model = OurTeam
    menu_label = 'Our Team'
    menu_icon = 'pick'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("position", "name", "last_name", )
    list_filter = ("position",)
    search_fields = ("position",  "name", "last_name",)


modeladmin_register(OurTeamAdmin)


class ContactAdmin(ModelAdmin):
    model = Contact
    menu_icon = 'pick'
    menu_label = 'Contact form'
    menu_order = 210
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "email", "message")
    list_filter = ("name", "email")
    search_fields = ("name", "email", "message")


modeladmin_register(ContactAdmin)