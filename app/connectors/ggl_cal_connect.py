from app.connectors.Connectable import IConnector


class GoogleCalendarConnector(IConnector):
    def __init__(self, credentials: dict):
        self.credentials = credentials

    def execute(self, action: str, payload: object) -> dict:

       match action:
           case "GOOGLECALENDAR_CREATE_EVENT":
               pass
           case "GOOGLECALENDAR_DUPLICATE_EVENT":
               pass

           case _:
               return


    def authenticate(self) -> bool:
        pass

    def 