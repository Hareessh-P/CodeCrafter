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
pip install django==4.1.13
pip install djongo==1.3.6
pip install pymongo==3.12.3
pip install djangorestframework==3.14.0
pip install django-cors-headers==4.3.1
pip install djangorestframework-simplejwt==5.3.1
pip install boto3==1.33.13
pip install django-extensions==3.2.3

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
## Backend Design
![Alt text](https://github.com/Hareessh-P/CodeCrafter/blob/master/design-images/instructor_pov_design.jpeg)


