from django.contrib import admin

# Register your models here.


from webapp.models import Guestbook

list_display = ['id', 'author', 'email', 'status', 'created_at']
list_display_links = ['author']
list_filter = ['status']
search_fields = ['author']
fields = ['author', 'status', 'created_at']


admin.site.register(Guestbook)