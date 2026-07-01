from django.contrib.auth.backends import UserModel
from django.db import models
from django.db.models import SET_NULL

from secure_notes.managers import ActiveNoteManager


# Create your models here.
class Note(models.Model):
    owner = models.ForeignKey(to=UserModel, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=100)
    body = models.TextField()
    is_deleted = models.BooleanField(default=False)  # 1. The Flag
    objects = ActiveNoteManager()  # 2. Automatically hides deleted ones
    all_objects = models.Manager()  # 3. For backend/moderator auditing

    # 4. Intercept the delete action
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()


