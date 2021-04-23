from django.contrib import admin

# Register your models here.
from content.models import Menu, Content, Images


class ContentImageInline(admin.TabularInline):
    model = Images
    extra = 5


class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'parent']
    list_filter = ['status']


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'menu', 'image_tag']
    readonly_fields = ['image_tag']
    list_filter = ['status', 'type']
    inlines = [ContentImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'image_tag']
    readonly_fields = ['image_tag']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Images, ImagesAdmin)
