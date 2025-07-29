from composio_llamaindex import ComposioToolSet

class ComposioService:
    def __init__(self):
        pass

    def authenticate(self, web_service: str) -> str:

        # check in the db if there are any composio credentials
        # if not, fetch from "api"
        # call on launch

        composio_toolset = ComposioToolSet()




        return ""

    def execute_connection(self, app, action, payload):
        pass

    def add_connector(self, connector) -> (str, str):
        # todo::: add connector to composio account
        if connector == "google_calendar":
            return "61lsia39d25b45nqftihia", "default"
        return None
