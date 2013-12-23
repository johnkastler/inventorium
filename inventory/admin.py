from django.contrib import admin
from inventory.models import Item

class ItemAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title','description']
    # fields to filter the change list with
    list_filter = ['created']
    # fields to search in change list
    search_fields = ['title','description']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
    # prepopulate the slug from the title - big timesaver !
    # prepopulated_fields = {"slug":("title",)}

admin.site.register(Item,ItemAdmin)
