from django.db import models
from djongo import models

from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, default='default@example.com')  
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)  # TODO use a more secure field for passwords

    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    course_description = models.TextField(null=True, blank=True)
    course_thumbnail_url = models.URLField()
    course_tags = models.JSONField()
    course_length = models.PositiveIntegerField()

class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=255)
    topic_asset_urls = models.JSONField()
    topic_asset_type = models.JSONField()
    topic_length = models.PositiveIntegerField()

class Asset(models.Model):
    asset_id = models.AutoField(primary_key=True)
    asset_type = models.CharField(max_length=50)
    asset_url = models.URLField()
    asset_length = models.PositiveIntegerField()
    asset_thumbnail = models.URLField()
