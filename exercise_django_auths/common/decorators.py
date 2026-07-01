from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import redirect


def editor_perm_required(group_name):
    """
    Custom decorator to restrict view access to a specific group role.
    """

    def decorator(editors_page):
        @wraps(editors_page)  # Keeps the original view function's metadata intact
        def wrapper(request, *args, **kwargs):

            # Scenario 1: User is not logged in (Anonymous)
            if not request.user.is_authenticated:
                return redirect('login')  # Redirects to your login URL pattern

            # Scenario 2: User is logged in, but not in the required group
            # (Superusers bypass this check automatically for convenience)
            if not request.user.groups.filter(name=group_name).exists() and not request.user.is_superuser:
                return HttpResponseForbidden(f"Access Denied: You must belong to the {group_name} group.")

            # Scenario 3: User passes all checks! Proceed to the view.
            return editors_page(request, *args, **kwargs)

        return wrapper

    return decorator