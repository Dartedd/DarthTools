import requests
import time
import sys

def spam_webhook(webhook_url, message, count, delay):
    for i in range(count):
        try:
            payload = {'content': message}
            response = requests.post(webhook_url, json=payload)

            if response.status_code == 204:
                print(f"Message {i + 1}/{count} sent successfully.")
            else:
                print(f"Failed to send message {i + 1}/{count}. Status code: {response.status_code}")

        except requests.RequestException as e:
            print(f"An error occurred: {e}")

        time.sleep(delay)

def main():
    webhook_url = input("Enter the Discord webhook URL: ").strip()
    message = input("Enter the message to send: ").strip()
    try:
        count = int(input("Enter the number of messages to send: ").strip())
        delay = float(input("Enter the delay between messages (in seconds): ").strip())
    except ValueError:
        print("Invalid input for count or delay. Please enter numeric values.")
        sys.exit(1)

    if not webhook_url or not message or count <= 0 or delay < 0:
        print("Invalid input. Please make sure all inputs are provided and valid.")
        sys.exit(1)

    spam_webhook(webhook_url, message, count, delay)

    # Pause before exiting
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
