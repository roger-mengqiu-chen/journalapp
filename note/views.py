from rest_framework.decorators import api_view
from rest_framework.response import Response

from note.note_services import get_note_by_id, get_notes_by_page
from note.serializers import NoteSerializer, NoteSummarySerializer


@api_view(['GET', 'DELETE', 'PUT'])
def note(request, note_id):

    note = get_note_by_id(note_id)
    if note is None:
        return Response({'message': 'Note not found'}, status=404)
    
    if request.method == 'GET':
        return Response(NoteSerializer(note).data)

    elif request.method == 'DELETE':
        note.delete()
        return Response({'message': 'Note deleted'}, status=204)
    

@api_view(['POST'])
def create_note():
    return Response({'message': 'note created'})


@api_view(['GET'])
def notes(request, page_number):
    notes = get_notes_by_page(page_number, note_per_page=10)
    res = NoteSummarySerializer(notes, many=True).data
    return Response({'notes': res})
