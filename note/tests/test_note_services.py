from django.test import TestCase
from note.models import Note, Tag
from note.note_services import get_note_by_id, get_notes_by_page, get_tags_and_notes_number, get_total_pages_of_notes


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


class TestGetTotalPagesOfNotes(TestCase):
    def setUp(self):
        Note.objects.all().delete()
        for i in range(0, 11):
            Note.objects.create(title=f'Test Note {i}', content=f'Test Content {i}')
    
    def test_get_total_pages_of_notes(self):
        total_pages = get_total_pages_of_notes()
        self.assertEqual(total_pages, 2)
    
    def test_get_total_pages_of_notes_not_found(self):
        Note.objects.all().delete()
        total_pages = get_total_pages_of_notes()
        self.assertEqual(total_pages, 1)


class TestGetTagsAndNotesNumber(TestCase):
    def setUp(self):
        Note.objects.all().delete()
        Tag.objects.all().delete()
        self.tag1 = Tag.objects.create(name='Tag 1')
        self.tag2 = Tag.objects.create(name='Tag 2')
    
    def test_get_tags_and_notes_number(self):
        note1 = Note.objects.create(title='Test Note 1', content='Test Content 1')
        note1.tags.add(self.tag1)
        note1.tags.add(self.tag2)
        note2 = Note.objects.create(title='Test Note 2', content='Test Content 2')
        note2.tags.add(self.tag1)

        tags_and_notes_number = get_tags_and_notes_number()
        self.assertEqual(len(tags_and_notes_number), 2)
        self.assertEqual(tags_and_notes_number['Tag 1'], 2)
        self.assertEqual(tags_and_notes_number['Tag 2'], 1)
    
    def test_get_tags_and_notes_number_not_found(self):
        Note.objects.all().delete()
        tags_and_notes_number = get_tags_and_notes_number()
        self.assertEqual(len(tags_and_notes_number), 2)
        self.assertEqual(tags_and_notes_number['Tag 1'], 0)
        self.assertEqual(tags_and_notes_number['Tag 2'], 0)
        