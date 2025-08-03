from typing import Dict

from app.Constants.Permissions import CEIO

ActionToPermissionMapper: Dict[str, int] = {}

ActionToPermissionMapper['GOOGLECALENDAR_CREATE_EVENT'] = CEIO.OBSERVE