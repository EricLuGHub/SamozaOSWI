
from composio_llamaindex import ComposioToolSet, Action

composio_toolset = ComposioToolSet(
    api_key="61lsia39d25b45nqftihia",
    entity_id="default"
)

result = composio_toolset.execute_action(
    action=Action(value="GOOGLECALENDAR_CREATE_EVENT"),
    params={
        "calendar_id": "primary",
        "summary": "Team Sync with Eric",
        "description": "Weekly catch-up with the team",
        "start_datetime": "2025-07-27T15:00:00-04:00",  # Required
        "event_duration_hour": 1,
        "event_duration_minutes": 0,
        "eventType": "default",
        "attendees": [],
        "guestsCanInviteOthers": True,
        "guestsCanSeeOtherGuests": True,
        "guests_can_modify": False,
        "create_meeting_room": True,
        "location": "Zoom",
        "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=FR"],
        "send_updates": True,
        "timezone": "America/Toronto",
        "transparency": "opaque",
        "visibility": "default"
    }
)


