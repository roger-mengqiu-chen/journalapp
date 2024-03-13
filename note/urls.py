from django.urls import path
from . import views


urlpatterns = [
    path('<int:page_number>', views.notes, name='notes'),
    path('<int:note_id>', views.note, name='notes'),
]




