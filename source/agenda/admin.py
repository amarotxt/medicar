from django.contrib import admin

# Register your models here.
from .models import Agenda
from .models import Horario

class HorarioInline(admin.TabularInline):
    model=Horario

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    inlines = [HorarioInline] 
    pass


# admin.site.register(Agenda)
