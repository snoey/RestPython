"# PythonRestApi" 
# RestPython

Step By step Run Apps Rest Registration Driver :
1.	Run on CMD >> git clone https://github.com/snoey/RestPython.git
2.	Run on CMD >> cd RestPython
3.	Run on CMD >>python –m venv env
4.	Run on CMD >>pipenv -–three
5.	Run on CMD >>pipenv shell
6.	Run on CMD >>python / pip install –r requirements.txt
Dependencies for file requirements.tx
flask==0.12.2flask_restful==0.3.6flask_script==2.0.6flask_migrate==2.1.1marshmallow==2.14.0flask_sqlalchemy==2.3.2flask_marshmallow==0.8.0
marshmallow-sqlalchemy==0.13.2psycopg2==2.7.5

7.	Create database gojek on postgres tolls (pgadmin or navicat)
8.	Run syntax on CMD >>: 
python migrate.py db init

 

9.	Run on CMD >>
python migrate.py db migrate

 


10.	Run on CMD >>
python migrate.py db upgrade
 

11.	Edit file RegistrationDriverDataCsv.py change directory 

with open('/Users/snoy/gojek/data/driver_registration.csv', 'r') as f:

Insert Data csv to database postgres

Run on CMD >>python RegistrationDriverDataCsv.py 
 

12.	Run on CMD >> python run.py

 



13.	Copy this link on browser : http://127.0.0.1:5000/

 
	




http://127.0.0.1:5000/RegistrationDriver


 

