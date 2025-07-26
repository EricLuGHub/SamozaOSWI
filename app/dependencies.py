from fastapi import Request

def get_auth_service(request: Request):
    return request.app.state.auth

def get_guard_service(request: Request):
    return request.app.state.guard

def get_wis_service(request: Request):
    return request.app.state.wis