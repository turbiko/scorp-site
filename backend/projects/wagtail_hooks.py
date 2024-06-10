from wagtail_modeladmin.options import ModelAdmin, modeladmin_register

from .models import Genre, ProjectGenres


class GenreAdmin(ModelAdmin):
    model = Genre
    menu_label = 'Genres'
    menu_icon = 'pick'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


modeladmin_register(GenreAdmin)


class ProjectGenresAdmin(ModelAdmin):
    model = ProjectGenres
    menu_label = 'Projects Genres'
    menu_icon = 'pick'
    menu_order = 220
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("page", "genre")
    list_filter = ("page", "genre")
    search_fields = ("page", "genre")


modeladmin_register(ProjectGenresAdmin)
