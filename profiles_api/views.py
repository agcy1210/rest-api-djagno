from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self, request, format=None):

        an_apiview = [
            'Uses HTTP methods as functions(GET, POST , PUT, PATCH, DELETE)',
            'It is similar to traditional Django view',
            'Gives you most control over logic',
            'Is mapped manually to urls'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
