from django.contrib import admin

# Register your models here.
from .models import Agenda
from .models import Horario

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    model = Agenda
    filter_horizontal = ('horarios',)
    


admin.site.register(Horario)
