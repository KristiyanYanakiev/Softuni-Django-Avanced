from django.urls import path
from secure_notes import views
from secure_notes.views import AddNote, NoteDeleteView

app_name = 'secure_notes'

urlpatterns = [
    path('', views.NotesList.as_view(), name='list'),
    path('moderators-notes-list', views.ModeratorsNotesList.as_view(), name='moderators-notes-list'),
    path('add-note/', AddNote.as_view(), name='add-note'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='delete-note')

]