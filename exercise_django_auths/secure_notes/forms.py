from django import forms
from secure_notes.models import Note


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['owner']


