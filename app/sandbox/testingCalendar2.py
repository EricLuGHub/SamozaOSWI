# filename: connect_and_fetch_github.py
from composio_llamaindex import ComposioToolSet, Action, App
from dotenv import load_dotenv
import sys


def run_auth_flow():
    user_id_in_my_app = "default" # Example user ID
    app_to_connect = App.GOOGLECALENDAR # Use Enum for clarity

    print(f"--- Starting GitHub connection for Entity: {user_id_in_my_app} ---")

    toolset = ComposioToolSet()
    entity = toolset.get_entity(id=user_id_in_my_app)

    active_connection = None # Initialize variable

    try:
        # --- 2. Initiate Connection ---
        print(f"Initiating {app_to_connect.value} connection...")
        # Use app_name; SDK finds appropriate integration
        connection_request = entity.initiate_connection(app_name=app_to_connect)

        # --- 3. Handle Redirect & Wait for Activation (OAuth) ---
        if connection_request.redirectUrl:
            print("\n!!! ACTION REQUIRED !!!")
            print(f"Please visit this URL to authorize the connection:\n{connection_request.redirectUrl}\n")
            print("Waiting for connection to become active (up to 120 seconds)...")

            try:
                # Poll Composio until the connection is marked active
                active_connection = connection_request.wait_until_active(
                    client=toolset.client, # Pass the underlying client
                    timeout=120
                )
                print(f"\nConnection successful! ID: {active_connection.id}")
                # In a real app, you'd store active_connection.id linked to user_id_in_my_app
            except Exception as e:
                print(f"Error waiting for connection: {e}", file=sys.stderr)
                print("Please ensure you visited the URL and approved the connection.")
                return # Exit if connection failed

        else:
            # Handle non-OAuth flows if needed (e.g., API Key where connection is instant)
            print("Connection established (non-OAuth flow). Fetching details...")
            # Fetch the connection details using the ID from the request
            active_connection = toolset.client.connected_accounts.get(connection_id=connection_request.connectedAccountId)
            if active_connection.status != "ACTIVE":
                 print(f"Connection is not active (Status: {active_connection.status}). Exiting.", file=sys.stderr)
                 return


        # --- 4. Execute Action ---
        if active_connection and active_connection.status == "ACTIVE":
            print(f"\nExecuting action using connection ID: {active_connection.id}")
            print(f"Fetching GitHub username for entity: {user_id_in_my_app}...")

            user_info = toolset.execute_action(
                action=Action.GITHUB_GET_THE_AUTHENTICATED_USER,
                params={},
                # Provide context via entity_id (recommended)
                entity_id=user_id_in_my_app
                # OR precisely target the connection (if ID was stored)
                # connected_account_id=active_connection.id
            )

            print("\n--- Execution Result ---")
            if user_info.get("successful"):
                username = user_info.get("data", {}).get("login", "N/A")
                print(f"Successfully fetched GitHub username: {username}")
            else:
                print(f"Failed to fetch user info: {user_info.get('error', 'Unknown error')}")
            # import json
            # print("\nFull response:")
            # print(json.dumps(user_info, indent=2))
        else:
             print("\nSkipping action execution as connection is not active.")


    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    run_auth_flow()
