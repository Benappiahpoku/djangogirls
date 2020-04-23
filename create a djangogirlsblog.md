# how to install pipenv globally on windows?
  - run cmd
  - python --version
  - pip --version
  - pip install pipenv 
  - pipenv --version

# how to create virtual environment?
  - pipenv install django==2.2.4

# how to acticate the virtual environment?
  - pipenv shell

# how to exit virtual environment?
  - exit
  
# how to make a project in django?
  - django-admin startproject mysite
  - cd mysite

# how to change settings in a project in django?
  - open settings.py file
  - change allowed hosts, time and Static root path

# how to set up the migrations in django?  
  - python manage.py migrate

# how to test everything is working in django?
  - python manage.py runserver
  - alt + link to view server
  - ctrl + c to cancel

# how to create an app in django?  
  - python manage.py startapp blog

# how to make INSTALED_APPS aware of the new app in django?  
  - settings.py in mysite 
  - blog.apps.BlogConfig

# how to create templates for the app?  
  - open blog > folder -> templates -> folder blog -> create .html files 
  - blog.apps.BlogConfig

# how to define oour models classes to create our database in django?  
  - update and edit models.py  

# how to create tables in your database in django?  
  - python manage.py makemigrations blog 

# how to apply new migrations into database in django?  
  - python manage.py migrate blog 

# how to add information into our newly created models in django?  
  - open admin.py to register the newly created model
  - python manage.py createsuperuser
  - http://127.0.0.1:8000/admin