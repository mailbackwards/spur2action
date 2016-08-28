# Texas Turnout

Spur To Action (S2A) is an interactive messaging service aiming to cultivate a civic engagement pipeline by connecting people to local issues that are relevant to their lives.  Through targeted information about San Antonio, S2A endeavors to empower individuals so they realize the potential to influence their community.

### Setup

`pip install -r requirements.txt`

Set the following environment variables with your Twilio credentials:

    TWILIO_ACCOUNT_SID
    TWILIO_AUTH_TOKEN

Then deploy to Heroku and link your Twilio phone # with the url `http://(your-domain-here).herokuapp.com/listen`.

Our Twilio phone #: '+12036800787'
