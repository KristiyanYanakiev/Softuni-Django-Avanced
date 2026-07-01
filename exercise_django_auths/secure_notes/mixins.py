from django.contrib.auth.mixins import PermissionRequiredMixin


class CanViewAllNotesPermissionRequiredMixin(PermissionRequiredMixin):

    permission_required = 'secure_notes.can_view_all_notes'