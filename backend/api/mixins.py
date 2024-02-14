from rest_framework import permissions

from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission
    ]

# can create other class permissions to allow certain users to access
    
# all of this below to avoid having to do it within the views.py. instead just link specific user to the request and SAVE TIME BY QUERYING ONLY FOR THE CURRENT USER
class UserQuerySetMixin():
    user_field = 'user'
    allow_staff_view = False # this to disallow staff (non-admins) to view requests
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user
        # print(lookup_data)
        qs = super().get_queryset(*args, **kwargs)
        # print(qs)
        if self.allow_staff_view and user.is_staff: # return qs if user is the staff user
            return qs
        return qs.filter(**lookup_data) # self.user_field = self.request.user