from django.contrib import admin
from .models import Page


# Register and Customize pages module in Admin, titles, ordering, search 
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('title',)
    search_fields = ('title', 'update_date')


admin.site.register(Page, PageAdmin)
