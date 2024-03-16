from note.models import Note


def get_note_by_id(id):
    try:
        note = Note.objects.get(note_id=id)
        return note
    except Note.DoesNotExist:
        return None


def delete_note_by_id(id):
    try:
        note = Note.objects.get(note_id=id)
        note.delete()
        return True
    except Note.DoesNotExist:
        return False


