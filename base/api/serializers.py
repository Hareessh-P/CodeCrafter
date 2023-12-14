from rest_framework import serializers
from base.models import User, Course, Topic, Asset , BulkUpload
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['role'] = user.role

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Include other fields as needed
        extra_kwargs = {'password': {'write_only': True}}

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


class BulkUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkUpload
        fields = [
            'bulk_upload_id',
            'user_id',
            'course_id',
            'bulk_upload_s3_url_temporary',
            'bulk_upload_name',
            'bulk_upload_time_date',
            'bulk_upload_status',
        ]
