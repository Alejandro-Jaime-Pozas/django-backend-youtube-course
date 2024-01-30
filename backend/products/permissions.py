from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):

    perms_map = {
    'GET': ['%(app_label)s.view_%(model_name)s'],
    'OPTIONS': [],
    'HEAD': [],
    'POST': ['%(app_label)s.add_%(model_name)s'],
    'PUT': ['%(app_label)s.change_%(model_name)s'],
    'PATCH': ['%(app_label)s.change_%(model_name)s'],
    'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    # has_permission checks if the user making the request has permission to view, add, change and/or delete
    def has_permission(self, request, view):
        # if user is not staff, deny access
        if not request.user.is_staff:
            return False 
        return super().has_permission(request, view) # this is the default permission
    
    # # this is a basic view for code learning: if user has permission, grant access (but code is granting access even if 1 condition is met for all conditions)
    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff: # if user has staff permissions configured in /admin
    #         # if user has permission to product app and to view the Product model, grant access
    #         if user.has_perm('products.add_product'): # IMPORTANT: in has_perm() include the <app_name>.<method>_<model_name> equivalents in django
    #             return True 
    #         if user.has_perm('products.change_product'): # 'view' 'change' 'add' 'delete' are all the GET, PUT, POST, DELETE method equivalents in django
    #             return True 
    #         if user.has_perm('products.delete_product'): # 'view' 'change' 'add' 'delete' are all the GET, PUT, POST, DELETE method equivalents in django
    #             return True 
    #         if user.has_perm('products.view_product'): # 
    #             return True 
    #         return False
    #     return False 
    
    # # also contains the obj, to check if obj belongs to user
    # def has_object_permission(self, request, view, obj):
    #     return super().has_object_permission(request, view, obj)