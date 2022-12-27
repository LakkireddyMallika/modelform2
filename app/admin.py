from django.contrib import admin

# Register your models here.
from app.models import *
class WebpageAdminView(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    #list_editable=['name']
    list_display_links=['topic_name','name']
    search_fields=['name']
    list_per_page=2
    list_filter=['name','topic_name']








admin.site.register(Topic)
admin.site.register(Webpage,WebpageAdminView)
admin.site.register(AccessRecords)