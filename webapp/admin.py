from django.contrib import admin

# Register your models here.


from webapp.models import Guestbook


class GuestbookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'status', 'created_at']
    list_display_links = ['author']
    list_filter = ['status']
    search_fields = ['author']
    fields = ['author', 'email', 'status', 'created_at', 'updated_at', 'text']
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(Guestbook, GuestbookAdmin)