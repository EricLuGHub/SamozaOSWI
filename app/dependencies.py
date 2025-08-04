from fastapi import Request


def get_wis_service(request: Request):
    return request.app.state.wis

def get_composio_service(request: Request):
    return request.app.state.composio_service

def get_badge_service(request: Request):
    return request.app.state.badge_service

def get_sap_service(request: Request):
    return request.app.state.sap_service