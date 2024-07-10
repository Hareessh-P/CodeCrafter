## Django project Set-up :

## Backend Design
![Alt text](https://github.com/Hareessh-P/CodeCrafter/blob/master/design-images/instructor_pov_design.jpeg)

## Design Decisions: 
- Micro-Service Architecture , because the video transcoding is memory and a compute intensive task. 
-  metric: transcoding a video of length 1hr may take 1.25 - 1.5 hrs - So the Authentication cum Video Upload service can handle many concurrent requests, instead of transcoding the videos. 
- Authentication mechanism is JWT(with RSA256) based , as it is scalable . Since we don't need to store the sessions in the database. 
- Blacklisting jwt token not working with the in-built django authentication system, as it was not compatible with the version of MongoDB, So introduced an in-memory Cache(Redis) to store blacklisted tokens until expiry. 
- Database used for Authentication and Video Upload Service was MongoDB. - Video files, Thumbnails, pdfs stored in Blob Storage. (S3) 
- Asynchronous Communication between Authentication cum Video Upload Service and Video Transcoder Service is achieved through RabbitMQ(Message Broker). - Video Transcoder is a serverless spot instance that is triggered by RabbitMQ. - A webhook is used to return s3 urls and delete temporary s3 files. 
- Use of pre-signed urls for upload from the frontend is very crucial as they provide an interface with AWS S3 so the video,etc that are uploaded are directly sent to the AWS servers managing s3 and our server is free, improving server performance or its availability.


## Backend workflow: 
- The user enters username and password in the frontend that is sent to the NGINX Proxy server, which in turn acts as an api gateway and redirects the api call to the respective service that is the Authentication cum Video upload service. 
- The service authenticates the user and sends the user a jwt token (access token + refresh token). 
- The access token is sent with every api call in the http header , and the refresh token is sent to the refresh api endpoint so that new access and refresh token is given blacklisting the old ones.The role: instructor is sent with the jwt. 
- The video upload request is sent to the Video upload service and then it responds with a pre-signed url where the user can upload the videos. This s3 bucket acts as a temporary storage as they need to be transcoded in a while. 
- The user in the frontend directly uploads the videos to the aws s3 bypassing the server.This improves the availability of the server. 
- The video urls that need to be transcoded are enqueued in the message broker , in our case RabbitMQ. 
- RabbitMQ triggers a spot-instance,which transcodes the video files and stores in the s3 with a new url, and sends a webhook to the Video Upload Service and temporary s3 files are deleted. 
- FFmpeg is used for Video files Transcoding.

## Technology Stack used: 
- Django - Authentication and Video Upload Service - FastAPI - Video Transcoder 
- MongoDB - Database 
- AWS S3 - BLOB Storage 
- RabbitMQ - Message Broker 
Concepts learned : 
- REST API 
- Webhook 
- S3 pre-signed url 
- S3 file storage structure (its Key-Value) 
- JWT 
- Access and Refresh Tokens 
- Asynchronous Communication 


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





