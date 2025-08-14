from typing import Dict

from app.Constants.Permissions import CEIO

ActionToPermissionMapper: Dict[str, int] = {}

ActionToPermissionMapper['GOOGLECALENDAR_CREATE_EVENT'] = CEIO.OUTPUT
ActionToPermissionMapper['GOOGLECALENDAR_DELETE_EVENT'] = CEIO.OUTPUT
ActionToPermissionMapper['GMAIL_CREATE_EMAIL_DRAFT'] = CEIO.OUTPUT
ActionToPermissionMapper['GMAIL_DELETE_DRAFT'] = CEIO.OUTPUT