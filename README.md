## Django project Set-up :

###   Python virtual environment setup
```
python -m venv env
env\Scripts\activate   # for Windows
# if u face any error , u have to set policy just chatGPT it :)
```
###   Clone my repo
```
git clone <my-https-url>
```
###   Djanog setup and installation
```
pip install django
pip install djongo
pip install pymongo==3.12.3
pip install djangorestframework
pip install django-cors-headers
pip install djangorestframework-simplejwt
pip install boto3
pip install django-extensions
```

###   MongoDB setup in docker
```
# Open new terminal
# To run mongodb in docker container
docker run -d
--name container_name
-e MONGO_INITDB_ROOT_USERNAME=username
-e MONGO_INITDB_ROOT_PASSWORD=password
-e MONGO_INITDB_DATABASE=DB_name
-p 27017:27017
xxx
#replace xxx with image id of the mongodb pulled
```
###  Run migrations
```
# Ensure that ur in the dir where manage.py exists
python manage.py makemigrations
python manage.py migrate
```
### Start server
```
python manage.py runserver
```
