from rest_framework import serializers

class HelloSerializer(serializers.Serializers):
    name = serializers.CharField(max_length=10)
    
