from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create HelloWorl apiview.

class HelloApiView(APIView):
    """Test APi View"""

    def get(self, request, format=None):
        """Return a list of APIView Features."""
    
        an_apiview =[
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'it is similiar to a traditional django framework',
            'Give you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello', 'data': an_apiview})