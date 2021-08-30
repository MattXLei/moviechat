DEFAULT_NOTIFICATION_PAGE_SIZE = 10


"""
"General" notifications include:
	1. FriendRequest
	2. FriendList
"""
# New 'general' notifications data payload incoming
GENERAL_MSG_TYPE_NOTIFICATIONS_PAYLOAD = 0
# No more 'general' notifications to retrieve
GENERAL_MSG_TYPE_PAGINATION_EXHAUSTED = 1
# Retrieved all 'general' notifications newer than the oldest visible on screen
GENERAL_MSG_TYPE_NOTIFICATIONS_REFRESH_PAYLOAD = 2
# Update a notification that has been altered (Ex: Accept/decline a friend request)
GENERAL_MSG_TYPE_UPDATED_NOTIFICATION = 5
