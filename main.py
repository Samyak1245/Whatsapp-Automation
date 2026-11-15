
import pywhatkit
import json
import re
from datetime import datetime


# Load saved contacts and groups
with open("recipients.json", "r") as file:
    recipients = json.load(file)


def get_recipient():

    print("\n1. Contact")
    print("2. WhatsApp Group")
    print("3. Enter phone number directly")

    choice = input("\nSelect recipient type: ").strip()

    if choice == "1":

        print("\nAvailable contacts:")
        for name in recipients["contacts"]:
            print("-", name)

        name = input("\nEnter contact name: ").strip().lower()

        if name not in recipients["contacts"]:
            raise ValueError("Contact not found!")

        return "contact", recipients["contacts"][name]

    elif choice == "2":

        print("\nAvailable groups:")
        for name in recipients["groups"]:
            print("-", name)

        name = input("\nEnter group name: ").strip().lower()

        if name not in recipients["groups"]:
            raise ValueError("Group not found!")

        return "group", recipients["groups"][name]

    elif choice == "3":

        number = input("Enter phone number with country code: ").strip()

        if not re.fullmatch(r"\+\d{8,15}", number):
            raise ValueError("Invalid phone number!")

        return "contact", number

    else:
        raise ValueError("Invalid selection!")


def schedule_message():

    try:

        recipient_type, recipient = get_recipient()

        message = input("\nEnter your message: ").strip()

        if not message:
            raise ValueError("Message cannot be empty!")

        date_input = input("Enter date (DD-MM-YYYY): ").strip()
        time_input = input("Enter time (HH:MM, 24-hour): ").strip()

        scheduled_time = datetime.strptime(
            f"{date_input} {time_input}",
            "%d-%m-%Y %H:%M"
        )

        if scheduled_time <= datetime.now():
            raise ValueError("Please enter a future date and time!")

        print("\n---------- MESSAGE DETAILS ----------")
        print("Recipient:", recipient_type)
        print("Message:", message)
        print("Scheduled:", scheduled_time.strftime("%d-%m-%Y %H:%M"))
        print("-------------------------------------")

        confirm = input("Schedule this message? (yes/no): ").strip().lower()

        if confirm != "yes":
            print("Message scheduling cancelled.")
            return

        if recipient_type == "contact":

            pywhatkit.sendwhatmsg(
                phone_no=recipient,
                message=message,
                time_hour=scheduled_time.hour,
                time_min=scheduled_time.minute,
                wait_time=25,
                tab_close=True
            )

        else:

            pywhatkit.sendwhatmsg_to_group(
                group_id=recipient,
                message=message,
                time_hour=scheduled_time.hour,
                time_min=scheduled_time.minute,
                wait_time=25,
                tab_close=True
            )

        print("\nMessage scheduling process completed!")

    except ValueError as error:
        print("Error:", error)

    except Exception as error:
        print("Something went wrong:", error)


if __name__ == "__main__":

    print("================================")
    print("     WHATSAPP MESSAGE SCHEDULER")
    print("================================")

    schedule_message()
