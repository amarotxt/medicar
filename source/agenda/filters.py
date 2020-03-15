from .models import Agenda
from django_filters import DateRangeFilter
from django_filters import DateFilter
from django_filters import FilterSet
from django_filters import ModelChoiceFilter
from django_filters import NumberFilter

class AgendaFilter(FilterSet):
    data_inicio = DateFilter(field_name='dia', lookup_expr=('gt'),)
    data_final = DateFilter(field_name='dia', lookup_expr=('lt'))
    especialidade = NumberFilter(method='filter_especialidade')

    class Meta:
        model = Agenda
        fields = ['data_inicio','data_final', 'medico','especialidade' ]

    def filter_especialidade(self, queryset, name, value):
        # raise Exception("aq")
        return queryset.filter(medico__especialidade=value)

    