from django.test import TestCase
from note.models import Note
from note.note_services import get_note_by_id, get_notes_by_page


class TestGetNoteById(TestCase):
    def setUp(self):
        Note.objects.all().delete()
        self.note = Note.objects.create(title='Test Note', content='Test Content')
    
    def test_get_note_by_id(self):
        note = get_note_by_id(self.note.note_id)
        self.assertEqual(note, self.note)
    
    def test_get_note_by_id_not_found(self):
        note = get_note_by_id(100)
        self.assertIsNone(note)
        

class TestGetNotesByPage(TestCase):
    def setUp(self):
        Note.objects.all().delete()
        for i in range(1, 11):
            Note.objects.create(title=f'Test Note {i}', content=f'Test Content {i}')
    
    def test_get_notes_by_page(self):
        notes = get_notes_by_page(1)
        self.assertEqual(len(notes), 10)
        self.assertFalse(notes.has_previous())
        self.assertFalse(notes.has_next())
    
    def test_get_notes_by_page_not_found(self):
        notes = get_notes_by_page(2)
        self.assertFalse(notes.has_previous())
        self.assertFalse(notes.has_next())
