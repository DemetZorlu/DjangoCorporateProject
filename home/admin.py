from django.contrib import admin
from home.models import Setting, ContactFormMessage, Profile


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'image_tag', 'status']
    readonly_fields = ['image_tag']


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'note', 'status']
    list_filter = ['status']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_name', 'city', 'image_tag']


admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Profile, ProfileAdmin)
