from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status


class HelloApiView(APIView):
    """Test API view"""

    serializer_class = serializers.HelloSerializer
    #important statement write in same format only

    def get(self, request, format=None):

        an_apiview = [
            'Uses HTTP methods as functions(GET, POST , PUT, PATCH, DELETE)',
            'It is similar to traditional Django view',
            'Gives you most control over logic', 'Is mapped manually to urls'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create hello message with our name """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {}".format(name)
            return Response({'message': message})

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object"""

        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in request"""

        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """Deletes an object"""

        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using routers',
            'provides more functionality with less code'
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})