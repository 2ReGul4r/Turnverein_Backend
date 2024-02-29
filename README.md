## Initial Project setup
```
From Turnverein_Backend Folder

#Windows
py -m venv venv

cd venv/Scripts/activate.bat

pip install django djangorestframework django-cors-headers
or
py -m pip install django djangorestframework django-cors-headers

#MacOs / Linux
python3 -m venv venv

. ./venv/bin/activate

pip install django djangorestframework django-cors-headers
or
python3 -m pip install django djangorestframework django-cors-headers
```

### Start project
```
From Turnverein_Backend Folder

#Windows
py manage.py runserver

#MacOs / Linux
python3 manage.py runserver
```

### Make Migrations
```
Migrations are needed to apply changes to there Database.
i.e. If you added a new model or edited one.

#Windows
py manage.py makemigrations Test
py manage.py migrate

#MacOs
python3 manage.py makemigrations Test
python3 manage.py migrate
````

### Backend Doku
```
Goto https://editor.swagger.io/
And drop the openapi.yaml in the left side.
```
