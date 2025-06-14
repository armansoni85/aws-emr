from rest_framework.permissions import BasePermission
from user.choices import RoleType
from user.models import CustomUser


class CanViewUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser or user.role in [
                RoleType.hospital_admin.value[0],
                RoleType.doctor.value[0],
            ]:
                return True
        return False


class CanCreateUser(BasePermission):
    """Checks the user create permission for the logged in user / current user"""

    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                return True

            if request.data["hospital"] != str(user.hospital_id):
                return False

            current_user_role = user.role
            # requested user role to be created
            requested_user_role = request.data["role"]
            if (
                current_user_role == RoleType.doctor.value[0]
                and requested_user_role == RoleType.patient.value[0]
            ):
                return True
            if current_user_role == RoleType.hospital_admin.value[
                0
            ] and requested_user_role in [
                RoleType.patient.value[0],
                RoleType.doctor.value[0],
            ]:
                # hospital admin cannot create hospital admin itself
                return True
        return False


class CanUpdateUser(BasePermission):
    """Checks the user update permission for the logged in user / current user"""

    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                return True

            if request.user.role == RoleType.hospital_admin.value[0]:
                if request.data["hospital"] == str(user.hospital_id):
                    return True

            if view.kwargs["pk"] == str(user.id):
                return True
        return False


class CanDeleteUser(BasePermission):
    """Checks the user delete permission for the logged in user / current user"""

    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                return True
            if user.role == RoleType.hospital_admin.value[0]:
                # hospital admin can delete its own hospital user only
                if CustomUser.objects.filter(
                    id=view.kwargs["pk"],
                    hospital_id=user.hospital_id,
                    role__in=[RoleType.patient.value[0], RoleType.doctor.value[0]],
                ).exists():
                    return True
        return False
