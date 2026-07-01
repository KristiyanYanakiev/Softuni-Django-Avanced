from django.db import models


class ActiveNoteManager(models.Manager):
    """
    Custom manager that automatically excludes soft-deleted records
    from standard database queries.
    """

    def get_queryset(self):
        # 1. Grab the default database query
        original_query = super().get_queryset()

        # 2. Silently attach the filter so deleted notes are hidden
        return original_query.filter(is_deleted=False)