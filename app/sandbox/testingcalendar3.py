# from composio_llamaindex import ComposioToolSet, Action, App
#
# toolset = ComposioToolSet()
# user_info = toolset.execute_action(
#                 action=Action.GOOGLECALENDAR_CREATE_EVENT,
#                 params={
#                     "calendar_id": "primary",
#                     "summary": "YOYOYO Sync with Eric",
#                     "description": "Weekly catch-up with the team",
#                     "start_datetime": "2025-08-02T15:00:00-04:00",  # Required
#                     "event_duration_hour": 1,
#                     "event_duration_minutes": 0,
#                     "eventType": "default",
#                     "attendees": [],
#                     "guestsCanInviteOthers": True,
#                     "guestsCanSeeOtherGuests": True,
#                     "guests_can_modify": False,
#                     "create_meeting_room": True,
#                     "location": "Zoom",
#                     "recurrence": [],
#                     "send_updates": True,
#                     "timezone": "America/Toronto",
#                     "transparency": "opaque",
#                     "visibility": "default"
#                 }
#                 ,
#                 entity_id="default",
#                 connected_account_id="4834305c-585b-45e9-a67e-c41577e30214"
#             )
#
# print(user_info)