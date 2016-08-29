import os
from flask import Flask, request, render_template, Response
from data import MESSAGES, REPLIES, NAMES
from twilio.rest import TwilioRestClient
from twilio import twiml

TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')

def send_text(recipient, body):
    client = TwilioRestClient()
    client.messages.create(
        to=recipient, from_=TWILIO_PHONE_NUMBER, body=body)

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_text_message():
    if 'type' in request.form:
        msg = MESSAGES[request.form.get('type')]
    else:
        msg = request.form.get('message')
    to = request.form.get('to')
    send_text(to, msg)
    return 'Success!'

@app.route('/listen', methods=['GET'])
def receive_text():
    req_body = request.values.get('Body', None)
    if req_body and req_body.strip().upper() in REPLIES:
        msg = REPLIES[req_body.strip().upper()]
        resp_body = msg['body']
    else:
        resp_body = "I didn't catch that. Come again?"

    media = REPLIES[req_body.strip().upper()].get('media', None)
    from_number = request.values.get('From', None)
    name = NAMES[from_number] if from_number in NAMES else 'there'

    resp = twiml.Response()
    msg = twiml.Message(resp_body, sender=TWILIO_PHONE_NUMBER)
    if media:
        msg.media(media[0])
    resp.append(msg)

    # extra catch for the demo
    if req_body.strip().upper() == 'T':
        supplemental = REPLIES['T-followup']['body']
        resp.message(supplemental, sender=TWILIO_PHONE_NUMBER)

    return Response(str(resp), mimetype='text/xml')

if __name__ == '__main__':
    app.run(debug=bool(os.environ.get('DEBUG')))
