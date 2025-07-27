from app.connectors.Connectable import BaseConnector


class GoogleCalendarConnector(BaseConnector):
    def __init__(self, api_key: str, entity_id: str, token: str = None):
        super().__init__(api_key, entity_id)
        self.connector_name = "GoogleCalendarConnector"


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