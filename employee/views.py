from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from employee.models import Employee_data
from datetime import datetime
from employee.forms import EmployeeForm,CondidateForm
from employee.filters import EmployeeFilter
import xlwt
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import auth
#from django.contrib.auth import logout,login,authenticate

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('home')
            else:
                pass
                messages.error(request, "Invalid username or password.")
        else:
            pass
            messages.error(request, "Invalid username or password.")


            return redirect('login')

    else:
        form = AuthenticationForm()
    return render(request,"login.html",{'form':form})
def logout(request):
    
    auth.logout(request)
    return redirect('login')


def home(request):
    dests = Employee_data.objects.all()
    count = Employee_data.objects.all().count()
    
    myFilter = EmployeeFilter(request.GET, queryset = dests)
    dests = myFilter.qs 

    return render(request,"home.html",{'dests': dests,'count' : count,'myFilter':myFilter})

def employee(request):

    if request.method == 'POST':
        full_name        = request.POST['full_name']
        gender           = request.POST['gender']

        if gender is None:
            messages.info(request,"Gender Required")
            print("********************gender required********************")

        email_id         = request.POST['email_id']
        phone_no         = str(request.POST['phone_no'])
        alternate_no     = str(request.POST['alternate_no'])
        date_of_birth    = request.POST['date_of_birth']
        date_of_birth    = datetime.strptime(date_of_birth, "%Y-%m-%d").strftime("%Y-%m-%d")

        year_of_exp      = request.POST['year_of_exp']
        job_position     = request.POST['job_position']
        current_ctc      = request.POST['current_ctc']
        expected_ctc     = request.POST['expected_ctc']
        current_company  = request.POST['current_company']

        skill_set           = request.POST.getlist('skill_set[]')
        skill_set        = ",".join(skill_set)

        work_Location       = request.POST['work_Location']
        preferred_location  = request.POST['preferred_location']
        negotiable          = request.POST['negotiable']
        currently_serving   = request.POST['currently_serving']
        in_days             = request.POST['in_days']
        reason_for_job_change = request.POST['reason_for_job_change']
        status               = request.POST['status']
        document        =   request.FILES['upolad_resume']
       
       #application_date    = request.POST['application_date']
        #application_date   = datetime.strptime(application_date, "%d/%m/%Y").strftime("%Y-%m-%d")


        employee_data  = Employee_data.objects.create(full_name = full_name,gender = gender ,email_id = email_id ,
                                                     phone_no = phone_no ,alternate_no = alternate_no ,
                                                     year_of_exp = year_of_exp ,
                                                     date_of_birth = date_of_birth ,
                                                     job_position = job_position,
                                                     current_ctc = current_ctc , 
                                                     expected_ctc = expected_ctc ,
                                                     current_company = current_company,
                                                     skill_set = skill_set ,
                                                     work_Location = work_Location ,
                                                     preferred_location = preferred_location ,
                                                     negotiable = negotiable ,
                                                     currently_serving = currently_serving ,
                                                     in_days = in_days ,
                                                     reason_for_job_change = reason_for_job_change ,
                                                     status = status ,
                                                     document = document
                                                     )
        employee_data.save()
        return redirect('home')

    return render(request,'add_employee_data.html')

def update_condidate_form(request,pk):

    data = Employee_data.objects.get(id=pk)
    form = CondidateForm(instance=data) 

    if request.method == 'POST':
        data = CondidateForm(request.POST, instance=data)
        if data.is_valid():
            data.save()
            return redirect('home')
    

    context = {'form':form}
    return render(request, 'upadate_condidate_form.html', context)
def delete_condidate_form(request, pk):
	
    item = Employee_data.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('home')

    context = {'item':item}
    return render(request, 'delete_condidate_form.html', context)
def view_condidate_form(request,pk):

    data = Employee_data.objects.get(id=pk)
    form = CondidateForm(instance=data)
    if request.method == "POST":
        return redirect('home')

    context = {'form':form}
    return render(request,"formdata.html",context)
def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/document")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404

def export_condidate_list(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="condidatelist.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Condidatelist')
 
    # Sheet header, first row
    row_num = 0
 
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
 
    columns = ['Full Name', 'Gender', 'Email Id', 'Phone No','Alternate No',
               'Year Of Exp','Date Of Birth','Job Position',
               'Current CTC','Expected CTC','Skill Set',
               'Work Location','Preferred Location','Negotiable',
               'Currently Serving','Notice Period',
               'Reason for Job Change','Document']
  
 
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
 
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
 
    rows = Employee_data.objects.all().values_list('full_name','gender', 'email_id', 'phone_no',
                                                   'alternate_no','year_of_exp','date_of_birth','job_position',
                                                   'current_ctc','expected_ctc','skill_set',
                                                   'work_Location','preferred_location','negotiable',
                                                   'currently_serving','in_days',
                                                   'reason_for_job_change','document')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
 
    wb.save(response)
    return response
