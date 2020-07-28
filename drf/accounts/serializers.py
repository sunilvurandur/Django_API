from rest_framework import serializers
from django.contrib.auth.models import User
from . models import advisors

from . models import booking

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
    
# advisor serializer
class advisorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = advisors
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = ('id','booking_time')
        def create(self, validated_data):
            book = booking.objects.create_book(validated_data['book'])
            return book
