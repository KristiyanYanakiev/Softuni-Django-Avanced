from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from secure_notes.forms import AddNoteForm
from secure_notes.mixins import CanViewAllNotesPermissionRequiredMixin
from secure_notes.models import Note

# Create your views here.
class NotesList(ListView):
    template_name = 'secure_notes/list.html'
    context_object_name = 'notes'

    def get_queryset(self):

        return Note.objects.filter(owner_id=self.request.user.id)


class ModeratorsNotesList(CanViewAllNotesPermissionRequiredMixin, NotesList):

    def get_queryset(self):
        return Note.objects.select_related('owner').all()


class AddNote(CreateView):
    template_name = 'secure_notes/add-note.html'
    form_class = AddNoteForm
    success_url = reverse_lazy('secure_notes:list')

    def form_valid(self, form):
        # 1. Hold the save operation so it doesn't crash on the NOT NULL constraint
        note = form.save(commit=False)

        # 2. Tie the note to the current logged-in user making the request
        note.owner = self.request.user

        # 3. Save it for real
        note.save()

        return super().form_valid(form)


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'secure_notes/note_confirm_delete.html'
    success_url = reverse_lazy('secure_notes:list')

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

