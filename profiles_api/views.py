from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    def get(self, request, format=None):
        an_apiview = [
            # GET
            'api info content'
            # POST

            # PATCH

            # PUT

            # DELETE

        ]

        return Response({'message': 'Testing', 'an_apiview': an_apiview})