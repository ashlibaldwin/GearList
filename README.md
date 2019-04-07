# GearListApp
Django app for making lists about stuff


#Running locally

### requirements
- pip
`python3 -m pip install --user --upgrade pip`

- virtual env
`python3 -m pip install --user virtualenv`


### steps
1. Navigate to the project root
2. start a new virtual environment 

`python3 -m virtualenv env`

3. install mysql dmg file from the [MySQL community server](https://dev.mysql.com/downloads/mysql/)
- once downloaded, double click to open and install the file, follow the prompts
- start the server


4. add the following line to your bash profile:

`export PATH=$PATH:/usr/local/mysql/bin`

5. restart the command line & naviate to the project root

6. drop into mysql shell

`$ mysql -u root -p`
Enter password:

7. create the database

`CREATE DATABASE gearlist;`
`CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password1';`
`GRANT ALL PRIVILEGES ON gearlist.* TO 'admin'@'localhost';`
`FLUSH PRIVILEGES;`
`quit`


7.1. python manage.py createsuperuser


7.2. activate the virtual env

`source env/bin/activate`

8. install requirements

`pip install -r requirements.txt`

9. migrate

`python manage.py migrate`

10. start the server:
`python manage.py runserver`

At this point the server should start and you can view the website locally at http://127.0.0.1:8000/

### Errors & troubleshooting:

- I got error like 'library not loaded, so I did this and it seemed to work:

`export DYLD_LIBRARY_PATH="/usr/local/mysql/lib:${DYLD_LIBRARY_PATH}"`
`export PATH="/usr/local/mysql/lib:${PATH}"`

- if new packages are added, run 
`pip install -r requirements.txt`

- sometimes deleting env and creating a new one fixes stuff


### To start the server next time, from the project root just run

`source env/bin/activate`
`python manage.py runserver`


