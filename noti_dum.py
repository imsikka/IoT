import pandas as pd
import schedule
import time
import logging
from twilio.rest import Client

# Twilio configuration
account_sid = 'ACbc54eeac8efd2bd527783d677406e080'
auth_token = '36e57482220dd9bcbcde5cdfc5986626'
twilio_client = Client(account_sid, auth_token)
twilio_phone_number = '+16575004860'
your_phone_number = '+918697171474'

# Set up logging
logging.basicConfig(filename='sms_log.txt', level=logging.INFO)

# Example function to control the AC
def turn_on_ac():
    # Add code to turn on the AC
    print("Turning on the AC")

def turn_off_ac():
    # Add code to turn off the AC
    print("Turning off the AC")

def read_person_count():
    try:
        # Read CSV file
        df = pd.read_csv('data.csv')  # Update the file name accordingly

        # Check if there are persons
        if 'no_of_persons' in df.columns:
            person_count = df['no_of_persons'].sum()

            # Send alert based on person count
            if person_count == 0:
                send_twilio_message("No person detected. TURN OFF THE LIGHTS.")
                turn_off_ac()  # Turn off the AC
            else:
                send_twilio_message(f"{person_count} persons detected. TURN ON THE LIGHTS .")
                turn_on_ac()  # Turn on the AC
        else:
            print("Error: 'no_of_persons' column not found in the CSV file.")
    except Exception as e:
        # Log any exceptions that occur during the job execution
        logging.error(f"Error in job execution: {str(e)}")

def send_twilio_message(message):
    try:
        # Send SMS using Twilio
        message = twilio_client.messages.create(
            from_=twilio_phone_number,
            to=your_phone_number,
            body=message
        )

        print(f"Message sent. SID: {message.sid}")

        # Log the successful message sent
        logging.info(f"Message sent successfully. SID: {message.sid}")

    except Exception as e:
        # Log any exceptions that occur during the message-sending process
        logging.error(f"Error sending message: {str(e)}")
        print(f"Error sending message: {str(e)}")

# Schedule the job every 5 seconds
schedule.every(5).seconds.do(read_person_count)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)

except KeyboardInterrupt:
    print("Script terminated by user.")
    logging.info("Script terminated by user.")
