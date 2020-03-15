from .models import Agenda
from django_filters import DateRangeFilter, DateFilter, FilterSet


class DateFilter(FilterSet):
    data_inicio = DateFilter(field_name='dia', lookup_expr=('gt'),)
    data_final = DateFilter(field_name='dia', lookup_expr=('lt'))
    # date_range = DateRangeFilter(name='dia')

    class Meta:
        model = Agenda
        fields = ['data_inicio','data_final' ]
