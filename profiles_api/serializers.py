from rest_framework import serializers


class HellowSerializer(serializers.Serializer):
    '''
    Serializes a name field for testing our API View
    '''

    name = serializers.CharField(max_length=10)
