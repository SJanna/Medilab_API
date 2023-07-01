from rest_framework import permissions

#Los distintos Roles/Grupos son: Recepcionistas, Doctores, Bacteriologos, Empresas --> También hay administradores,
#pero los definimos directamente con IsAdminUser que trae .permmissions por defecto, que verificia si
#el usuario is_staff.

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Verificar si el usuario autenticado es el propietario o un administrador
        return obj == request.user or request.user.is_staff
