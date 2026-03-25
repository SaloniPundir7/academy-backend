from rest_framework.permissions import BasePermission

class IsCourseOwner(BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


    def has_object_permission(self, request, view, obj):

     if obj.__class__.__name__ == "Course":
        return obj.created_by == request.user

     if obj.__class__.__name__ == "Lesson":
        return obj.course.created_by == request.user

     return False