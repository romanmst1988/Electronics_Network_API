from rest_framework.permissions import BasePermission


class IsActiveEmployee(BasePermission):
    message = "Доступ к API разрешен только активным сотрудникам."

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.is_active
            and request.user.is_staff
        )