from app.connectors.Connectable import BaseConnector


class GoogleCalendarConnector(BaseConnector):
    def __init__(self):
        # get from db or set none
        self.credentials = None


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

    def ggl_cal_create_event(self, payload: dict) -> dict:
        pass