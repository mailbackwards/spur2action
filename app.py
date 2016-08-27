import os
from flask import Flask, request, render_template, Response
from twilio.rest import TwilioRestClient
from twilio import twiml

TWILIO_PHONE_NUMBER='+12036800787'

NAMES = {
    '+12036067072': 'Liam',
}

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
    body = request.values.get('Body', 'no message here!')
    from_number = request.values.get('From', None)
    name = NAMES[from_number] if from_number in NAMES else 'there'

    resp = twiml.Response()
    resp.message('hello %s, %s' % (name, body), sender=TWILIO_PHONE_NUMBER)
    return Response(str(resp), mimetype='text/xml')

if __name__ == '__main__':
    app.run(debug=bool(os.environ.get('DEBUG')))
