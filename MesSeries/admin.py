from django.contrib import admin
from MesSeries.models import  Serie




class SerieAdmin(admin.ModelAdmin):
    list_display = ('nom','langue', 'type')
    list_filter = ('nom', 'langue')
    date_hierarchy = 'dateDiffusion'
    ordering = ('dateDiffusion',)
    search_fields = ('nom', 'type') 
    


admin.site.register(Serie,SerieAdmin)


