import django_filters
from django_filters import DateFilter, CharFilter

from employee.models import *

class EmployeeFilter(django_filters.FilterSet):
	#start_date = DateFilter(field_name="application_date", lookup_expr='gte')
	#end_date = DateFilter(field_name="application_date", lookup_expr='lte')
	#skills = django_filters.CharFilter(lookup_expr='icontains')
	#duration = django_filters.NumberFilter()
	#jobpo = django_filters.CharFilter(lookup_expr='icontains')


	class Meta:
		model = Employee_data
		#fields = ['job_position','skill_set','year_of_exp']
	#	exclude = ['customer', 'date_created']

		fields = {'job_position': ['icontains'],
				  'skill_set': ['icontains'],
		          'year_of_exp': ['exact'],
                  'job_position': ['icontains'],
                 }