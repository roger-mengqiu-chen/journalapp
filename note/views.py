from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def note(request, note_id):
    return Response({'note': 'note'})


@api_view(['GET'])
def notes(request, page_number):
    return Response({'notes': 'notes'})
