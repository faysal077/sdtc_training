from django.core.exceptions import PermissionDenied

class CenterAccessMixin:
    """
    Use in ListView / DetailView etc.
    Requires that views define `model` or `queryset`.
    Superusers see all; normal users limited to their center (profile.center).
    """
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.is_superuser:
            return qs
        profile = getattr(user, 'profile', None)
        if not profile or not getattr(profile, 'center', None):
            # If user has no center assigned, deny or return empty queryset
            return qs.none()
        center = profile.center
        # We assume related field name on model is center or Center FK
        return qs.filter(center=center)
