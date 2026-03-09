from parser import extract_details
from sheets import save_to_google_sheet
from calendar_event import schedule_call

def main():

    with open("data/sample_message.txt", "r") as f:
        message = f.read()

    data = extract_details(message)

    print("\nExtracted Information")
    print("---------------------")

    for key, value in data.items():
        print(f"{key}: {value}")

    save_to_google_sheet(data)

    schedule_call(data)

    print("\nData saved to Google Sheets")
    print("Calendar event created")

if __name__ == "__main__":
    main()