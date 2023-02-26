from twilio.rest import Client

TWILIO_SID = "AC29b90230f83ecb2ec40116cb5de7e16c"
TWILIO_AUTH_TOKEN = "099104ede72c293d42b7c5aba809853b"
TWILIO_VIRTUAL_NUMBER = '+16812532298'
TWILIO_VERIFIED_NUMBER = '+919135989874'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)