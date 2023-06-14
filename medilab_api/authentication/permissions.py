from rest_framework.permissions import BasePermission, SAFE_METHODS

#Los distintos Roles/Grupos son: Recepcionistas, Doctores, Bacteriologos, Empresas --> También hay administradores,
#pero los definimos directamente con IsAdminUser que trae .permmissions por defecto, que verificia si
#el usuario is_staff.

class IsReceptionistUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        group = user.groups

        if group.name == 'Receptionist':
            return True
        return False

class IsDoctorUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        group = user.groups

        if group.name == 'Doctor':
            return True
        return False
    
class IsBacteriologistUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        group = user.groups

        if group.name == 'Bacteriologist':
            return True
        return False
    
class IsCompanyUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        group = user.groups

        if group.name == 'Company':
            return True
        return False