from urllib.request import Request


def get_composio_service(request: Request):
    return request.app.state.composio_service

def get_credential_service(request: Request):
    return request.app.state.credential_service