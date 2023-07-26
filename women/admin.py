from django.contrib import admin
from women.models import Women


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'content',
                    'photo',
                    'is_published',
                    'time_create',
                    'time_update'
                    )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


admin.site.register(Women, WomenAdmin)
