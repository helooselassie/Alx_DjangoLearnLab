from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ensures password is not returned in responses

    class Meta:
        model = User  # Use your custom user model
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user with hashed password
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        
        # Create an authentication token for the user
        Token.objects.create(user=user)
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # Using CharField to validate username input
    password = serializers.CharField()  # Using CharField to validate password input

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid username or password.")
            data['user'] = user
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Use your custom user model
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user with hashed password
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        
        return user


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Use your custom user model
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user with hashed password
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        
        # Create an authentication token for the new user
        Token.objects.create(user=user)
        return user
