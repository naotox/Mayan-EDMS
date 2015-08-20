from __future__ import unicode_literals

from django.contrib import admin

from .models import MetadataType


class MetadataTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'label', 'default', 'lookup', 'validation', 'parser'
    )


admin.site.register(MetadataType, MetadataTypeAdmin)
