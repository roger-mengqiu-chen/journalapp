from django.urls import path
from . import views


urlpatterns = [
    path('notes/<int:page_number>', views.notes, name='notes'),
    path('<int:note_id>', views.note, name='notes'),
    path('new', views.create_note, name='create_note')
]




