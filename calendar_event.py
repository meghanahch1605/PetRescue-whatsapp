from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle
from datetime import datetime, timedelta

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_credentials():

    creds = None

    if os.path.exists("token_calendar.pickle"):
        with open("token_calendar.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            "client_secret.json", SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open("token_calendar.pickle", "wb") as token:
            pickle.dump(creds, token)

    return creds


def schedule_call(data):

    creds = get_credentials()

    service = build("calendar", "v3", credentials=creds)

    start = datetime.utcnow() + timedelta(minutes=5)
    end = start + timedelta(minutes=30)

    event = {
        "summary": "Pet Rescue Follow-up",
        "description": f"WhatsApp call with {data['owner']} ({data['phone']})",
        "start": {"dateTime": start.isoformat() + "Z"},
        "end": {"dateTime": end.isoformat() + "Z"}
    }

    service.events().insert(calendarId="primary", body=event).execute()

    print("Calendar event created")