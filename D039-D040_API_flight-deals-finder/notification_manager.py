"""This class is responsible for sending notifications with the deal flight details.
"""

from twilio.rest import Client
import os

SMS_API_KEY = os.environ.get('SMS_API_KEY')
SMS_SID = os.environ.get('SMS_SID')
TWILIO_NUMBER = os.environ.get('NUMBER')


class NotificationManager:

    def send_message(self, message):
        account_sid = SMS_SID
        auth_token = SMS_API_KEY
        client = Client(account_sid, auth_token)

        sms = client.messages \
            .create(body=message, from_=TWILIO_NUMBER, to='my_number')
        print(sms.status)

    # TODO: Create a send_mail method to send email with flight deals to all people joined in the "users" google
    #  spreadsheet
