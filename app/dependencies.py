from fastapi import Request

# return request.app.state.composio

def get_auth_service(request: Request):
    return None

def get_guard_service(request: Request):
    return None

def get_wis_service(request: Request):
    return request.app.state.wis

def get_composio_service(request: Request):
    return None

def get_badge_service(request: Request):
    return None