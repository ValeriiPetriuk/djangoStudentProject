from rest_framework.permissions import BasePermission


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
       
        return request.user.id != None and request.user.role == 'Teacher'
