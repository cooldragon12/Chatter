"""
Building Blocks specific for the Chats, Room Functionality.

This custom mixin will making the view more easily to implement and to lessen redanduncy.
NOTE: The structure of the mixin will be base on built-in mixin to make it easier to implement in other view. 
"""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model

User = get_user_model()

class JoinRoomMixin:
    """
    Join to a Room. Will update the the room model instance
    """
    @action(methods=['put'], detail=False)
    def join(self, request, *args, **kwargs):
        """
        Using the lookup field to get the instance object
        """
        instance = self.get_object() # get the room, user will join in if exist
        serializer = self.get_serializer(instance=request.data, data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, username=request.COOKIES.get('user').id)
        if instance in user.members_in_room.all():
            # If the room is one of the users joined in
            # Then the user will not able to join
            return Response({"message":f"You have already joined"}, status.HTTP_400_BAD_REQUEST)

        # If not exist user will able to join
        serializer.do_join(instance,user)
        

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response({"message":f"You have successfully joined"}, status.HTTP_200_OK)
    
class LeaveRoomMixin:
    """
    Leave to a Room. Will update the the room model instance
    """
    @action(methods=['get'], detail=False)
    def leave(self, request, *args, **kwargs):
        
        instance = self.get_object()
        serializer = self.get_serializer(instance=request.data, data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, username=serializer.data.get('username'))
        if instance not in user.members_in_room.all():
            # If the room is one of the users joined in
            # Then the user will not able to join
            return Response({"message":f"You're not belong to this group"}, status.HTTP_400_BAD_REQUEST)
        
        serializer.do_leave(instance, user)
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response({"message": f"Good bye"}, status.HTTP_200_OK)

