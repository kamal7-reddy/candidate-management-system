from django.forms import ModelForm
from employee.models import Employee_data


class EmployeeForm(ModelForm):
	class Meta:
		model = Employee_data
		fields = ['job_position','skill_set','year_of_exp']


class CondidateForm(ModelForm):
	class Meta:
		model = Employee_data
		fields = '__all__'

