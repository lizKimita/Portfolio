from django.contrib import admin
from .models import Project, languages, User


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal =('languages',)

admin.site.register(User)
admin.site.register(Project,ProjectAdmin)
admin.site.register(languages)

