from django.contrib import admin
from home.models import Setting


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'image_tag', 'status']
    readonly_fields = ['image_tag']


admin.site.register(Setting,SettingAdmin)