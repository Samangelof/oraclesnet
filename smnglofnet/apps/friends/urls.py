from django.urls import path, include
from friendship.models import Friend, Follow, Block
from friendship.views import (
    all_users,
    block_add,
    block_remove,
    blockers,
    blocking,
    follower_add,
    follower_remove,
    followers,
    following,
    friendship_accept,
    friendship_add_friend,
    friendship_cancel,
    friendship_reject,
    friendship_request_list,
    friendship_request_list_rejected,
    friendship_requests_detail,
    view_friends,
)



urlpatterns = [
    # ------------------------------------------------
    # ALL USERS
    path('users/', view=all_users, name="friendship_view_users"),

    # ------------------------------------------------
    # ADD FRIEND
    path('friend/add/<slug:to_username>/', view=friendship_add_friend,name="friendship_add_friend",),

    # ------------------------------------------------
    # ACCEPT FRIEND
    path('friend/accept/<int:friendship_request_id>/', view=friendship_accept,name="friendship_accept",),
    
    # ------------------------------------------------
    # REJECT FRIEND
    path('friend/reject/<int:friendship_request_id>/', view=friendship_reject,name="friendship_reject",),

    # ------------------------------------------------
    # FRIEND VIEW
    path('friends/<slug:username>/', view=view_friends, name="friendship_view_friends",),
]