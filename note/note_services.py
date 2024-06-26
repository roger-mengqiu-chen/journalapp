from note.models import Note, Tag
from django.core.paginator import Paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def get_note_by_id(id):
    try:
        note = Note.objects.get(note_id=id)
        return note
    except Note.DoesNotExist:
        return None


def get_notes_by_page(page_number, note_per_page=10):
    notes = Note.objects.all().order_by('-updated_at')
    paginator = Paginator(notes, note_per_page)

    try:
        notes = paginator.page(page_number)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)

    return notes


def get_total_pages_of_notes(note_per_page=10):
    notes = Note.objects.all().order_by('-updated_at')
    paginator = Paginator(notes, note_per_page)
    return paginator.num_pages


def get_tags_and_notes_number():
    tags = Tag.objects.all()
    tags_and_notes_number = {}
    for tag in tags:
        note_count = tag.note_set.count()
        tags_and_notes_number.update({tag.name: note_count})
    return tags_and_notes_number
