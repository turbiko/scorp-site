from django.contrib import admin

from projects.models import Genre, ProjectGenres, Project

# Register your models here.
admin.site.register(Genre)
admin.site.register(ProjectGenres)
admin.site.register(Project)

