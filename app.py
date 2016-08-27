import os
from flask import Flask, request, render_template
from twilio.rest import TwilioRestClient

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

if __name__ == '__main__':
    app.run(debug=bool(os.environ.get('DEBUG')))
