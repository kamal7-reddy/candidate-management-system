# candidate-management-system

Setup Django Appilcation 

1.create virtualenv  , excute below cammans
	pip install virualenv       // installing the virual env
	virtualenv name	// creatings the env name
	cms\scripts\activate		// activateing env
  
2.then install requirement.txt this file is had ala required cammands for application
	pip install -r requirment.txt
3.then install suitable database for the Django version
	After install database ,change in the setting.py file
	# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': 'Ielektron',                  // database name
        'USER': 'postgres',					// username
        'PASSWORD':'12345',				//password 
        'HOST':'localhost',				//Host

    }
	}
4.the migate the file excute below commands
	 
	1  >   python manage.py makemigration
	2  >   pyhton manage.py migrate
5.then excute the command for run the server
	1  >  python manage.py runserver


5. enter host name in browser for opening a application
6.in that application asking login credentials for l user login ,befor that we can create super user to our application using below cammands
	1  >  python manage.py createsuperuser
 
7. after creating the super user .we can login into the admin page then  we can add user and give permissions 
8. using  user login creadential we can login into the Candidate management system dash borad

Features of candidate management system 
•	.In that dash board we have 6 features and showing list applications and filters are the using filter we can filter the list of applications
1.	Add employee button : when you click on they open one window for adding the employee informations
2.	Export Button : this button for geneating the excel sheet for the list of application
3.	Edit button: using edit button we can edit the employee record
4.	Delete Button : using delete button we can delete the employee record
5.	View Button : using view Button we can see the employee Record  
