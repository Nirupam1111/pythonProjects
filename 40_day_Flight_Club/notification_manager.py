from twilio.rest import Client
import smtplib


TWILIO_SID = 'ACf7ad60669dd63ab3a60ed24fa67cfc88'
TWILIO_AUTH_TOKEN = '39ca7032261d065b7daa36eb1e439d93'
TWILIO_VIRTUAL_NUMBER = '+17123773008'
TWILIO_VERIFIED_NUMBER = '+919476467259'
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = 'nirupamsur10@gmail.com'
MY_PASSWORD = 'zxcvbnm@1'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
