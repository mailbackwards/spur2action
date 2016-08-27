from twilio.rest import TwilioRestClient

TWILIO_PHONE_NUMBER='+12036800787'


def send_text(recipient, body):
    client = TwilioRestClient()
    message = client.messages.create(
        to=recipient, from_=TWILIO_PHONE_NUMBER, body=body)
