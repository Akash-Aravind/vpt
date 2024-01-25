from django.contrib import admin
from root.models import DICT


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(DICT, AuthorAdmin)