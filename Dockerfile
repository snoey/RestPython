FROM python:3.6.7
RUN mkdir /gojek
WORKDIR /gojek
ADD . /gojek  
RUN /bin/sh -c pip install pipenv
RUN /bin/sh -c /bin/sh -c pipenv --three
RUN /bin/sh -c /bin/sh -c pipenv shell
RUN /bin/sh -c pip install -r requirements.txt
RUN /bin/sh -c /bin/sh python manage.py db init
RUN /bin/sh -c /bin/sh python manage.py db migrate
RUN /bin/sh -c /bin/sh python python manage.py db upgrade
RUN /bin/sh -c /bin/sh python python RegistrationDriverDataCsv.py
RUN /bin/sh -c /bin/sh python run.py

EXPOSE 5000