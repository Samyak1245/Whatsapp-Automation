# WhatsApp Message Scheduler

A Python-based WhatsApp automation project that allows users to schedule messages to individual contacts and WhatsApp groups using PyWhatKit.

## Features

- Schedule WhatsApp messages for individual contacts.
- Schedule messages for WhatsApp groups.
- Select recipients using saved contact or group names.
- Send messages directly using a phone number.
- Customize message content.
- Set the scheduled time.
- Confirm message details before scheduling.
- Case-insensitive contact and group name lookup.

## Technologies Used

- Python
- PyWhatKit
- JSON
- Regular Expressions
- Datetime

## Project Structure

```text
WhatsApp-Automation/
│
├── main.py
├── recipients.example.json
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements

- Python 3.10 or later
- Google Chrome or another supported browser
- WhatsApp account
- Internet connection
- WhatsApp Web login

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/Samyak1245/Whatsapp-Automation.git
```

**2. Navigate to the project directory**

```bash
cd Whatsapp-Automation
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure recipients**

Create a file named `recipients.json` in the project directory.

Use the following format:

```json
{
    "contacts": {
        "Shamik": "+91XXXXXXXXXX",
        "Shlok": "+91XXXXXXXXXX"
    },
    "groups": {
        "Friends": "YOUR_GROUP_ID"
    }
}
```

Replace the sample phone numbers and group ID with your own details.

Note: Keep `recipients.json` private. It is excluded from the Git repository.

## How to Find a WhatsApp Group ID

1. Open WhatsApp Web.
2. Open the required group.
3. Copy the group invite link.
4. Identify the group ID if supported by the link format and the PyWhatKit version you are using.

Do not share private group invite links publicly.

## Usage

**1. Run the Python program**

```bash
python main.py
```

**2. Select the recipient type**

- Contact
- WhatsApp Group
- Enter phone number directly

**3. Enter the required details**

- Recipient name or phone number
- Message content
- Scheduled time

**4. Confirm the message**

Review the details and enter `yes` to proceed with scheduling.

PyWhatKit opens WhatsApp Web and performs the scheduling process.

## Important Notes

- WhatsApp Web must be logged in before sending messages.
- Your computer must remain powered on and connected to the internet.
- The browser must remain available for the scheduled operation.
- Test the application with your own account before using it for important messages.
- Use this project responsibly and respect recipients' privacy and consent.
- Automated messaging may be subject to WhatsApp's terms and restrictions.

## Future Improvements

- Graphical user interface using Tkinter.
- Support for multiple scheduled messages.
- Message history and logging.
- Support for images and document attachments.
- Improved scheduling for future dates.
- Better error handling and validation.

## Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork this repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## Author

**Samyak Pusate**

GitHub: [@Samyak1245](https://github.com/Samyak1245)

---

If you find this project useful, consider giving the repository a ⭐ on GitHub!
