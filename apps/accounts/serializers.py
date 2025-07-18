from rest_framework import serializers

from apps.accounts.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role', 'avatar', 'date_joined','password','password_confirm',)
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def validate(self, attrs):
        if attrs.get('password')!= attrs.pop('password_confirm'):
            raise serializers.ValidationError("Passwords do not match.")
        return attrs
    
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['role'] = instance.get_role_display()
        return data
    
    @staticmethod
    def validate_username(value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value
    
    @staticmethod
    def validate_email(value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value
        
        
        