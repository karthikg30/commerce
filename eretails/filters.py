from .models import *
import django_filters
from django_filters import DateFilter

class OrderFilter( django_filters.FilterSet):
    start_date = DateFilter(field_name= "date_created", lookup_expr = "gte" )
    end_date = DateFilter(field_name= "date_created", lookup_expr = "lte" )
    class Meta:
        model = order
        fields = '__all__'
        exclude = ['customer','date_created', 'date_modified', 'm_user']