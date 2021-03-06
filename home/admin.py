from django.contrib import admin
from home.models import Setting, ContactFormMessage, FAQ


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'image_tag', 'status']
    readonly_fields = ['image_tag']


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'note', 'status']
    list_filter = ['status']


class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'ordernumber', 'answer', 'status']
    list_filter = ['status']

admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(FAQ, FAQAdmin)

