# from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from profiles_api import serializers

from rest_framework import viewsets

from profiles_api import models

from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions

from rest_framework import filters

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """
    Handles creating, reading and updating profile feed items
    """

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerialier
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    # @override
    def perform_create(self, serializer):
        '''
        sets the user profile to the logged in user
        '''

        serializer.save(user_profile=self.request.user)


class UserLoginApiView(ObtainAuthToken):
    '''
    Handle creating user authentication tokens
    '''

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class HelloApiView(APIView):
    '''
    Test API View
    '''
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''
        Returns a list of API View features
        '''
        an_apiview = [
            'Uses HTTP methods as functions (get, post, path, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({"message": "hello", 'an_apiview': an_apiview})

    def post(self, request):
        '''
        Create a hello message with our name
        '''

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        '''
        Handle updating an object
        '''

        return Response({'methond': 'PUT'})

    def patch(self, request, pk=None):
        '''
        Handle a partial update of an object
        '''

        return Response({'methond': 'PATCH'})

    def delete(self, request, pk=None):
        '''
        Handle a partial update of an object
        '''

        return Response({'methond': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """
    Test api view set
    """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """
        Return a hello message
        """

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update, destory)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({"message": "hello!", "a_viewset": a_viewset})

    def create(self, request):
        """
        create a new hello message
        """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """
        Handle getting an object by its ID
        """

        return Response({'HTTP method': 'GET'})

    def update(self, request, pk=None):
        """
        Handle update an object by its ID
        """

        return Response({'HTTP method': 'UPDATE'})

    def partial_update(self, request, pk=None):
        """
        Handle partial update an object by its ID
        """

        return Response({'HTTP method': 'PATCH'})

    def destroy(self, request, pk=None):
        """x
        Handle remove an object by its ID
        """

        return Response({'HTTP method': 'DELETE'})
