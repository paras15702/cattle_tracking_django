import django_filters
from django_filters import DateFilter,CharFilter
from .models import *

class CattleFilter(django_filters.FilterSet):
    class Meta:
        model=Cattle
        fields=['name','breed','age','pregnant','lost_status']
        

class FarmerFilter(django_filters.FilterSet):
    class Meta:
        model=Farmer
        fields=['name','address','contact']        