from rest_framework.decorators import api_view
from rest_framework.response import Response

from note.models import Note
from note.serializers import NoteSerializer


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def note(request, note_id):
    note_1 = Note.objects.get(note_id=note_id)
    res = NoteSerializer(note_1).data
    return Response(res)


@api_view(['GET'])
def notes(request, page_number):
    return Response({'notes': 'notes'})
