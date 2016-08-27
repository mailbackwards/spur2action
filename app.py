import os
from flask import Flask, request, render_template, Response
from data import MESSAGES, NAMES
from twilio.rest import TwilioRestClient
from twilio import twiml

TWILIO_PHONE_NUMBER='+12036800787'

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
    body = request.form.get('body')
    send_text('+12036067072', body)
    return 'Success!'

@app.route('/listen', methods=['GET'])
def receive_text():
    req_body = request.values.get('Body', None)
    if req_body and req_body.strip().upper() in MESSAGES:
        msg = MESSAGES[req_body.strip().upper()]
        resp_body = msg['body']
    else:
        resp_body = "I didn't catch that. Come again?"

    from_number = request.values.get('From', None)
    name = NAMES[from_number] if from_number in NAMES else 'there'

    resp = twiml.Response()
    resp.message(resp_body, sender=TWILIO_PHONE_NUMBER)
    return Response(str(resp), mimetype='text/xml')

if __name__ == '__main__':
    app.run(debug=bool(os.environ.get('DEBUG')))
