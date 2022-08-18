from twilio.rest import Client

TWILIO_SID = 'ACf7ad60669dd63ab3a60ed24fa67cfc88'
TWILIO_AUTH_TOKEN = '39ca7032261d065b7daa36eb1e439d93'
TWILIO_VIRTUAL_NUMBER = '+17123773008'
TWILIO_VERIFIED_NUMBER = '+919476467259'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
