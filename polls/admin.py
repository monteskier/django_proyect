from django.contrib import admin
from polls.models import Polls, Opciones

class OpcionesInline(admin.TabularInline):
    model = Opciones
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                      {'fields': ['preguntas']}),
        ('Informacio del Tiempo',   {'fields': ['pub_fecha'], 'classes': ['collapse']}),

    ]
    inlines = [OpcionesInline]

    list_display = ('preguntas', 'pub_fecha', 'was_published_recently')

    list_filter = ['pub_fecha']
    search_fields = ['preguntas']





admin.site.register(Polls, PollAdmin)
