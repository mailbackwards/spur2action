MESSAGES = {
    'prop1': 'Prop 1 is on Saturday, May 7. Practice voting and see what happens! Text YES or NO.',
    'prop1-snack': "Reducing the number of cars on SA's roads will help move people faster.",
    'prop1-prevote': ('The ridesharing election is tomorrow! '
        "Send us your zip code and we'll let you know where your closest polling place is."),
    'prek': 'Prop PREK4SA is on Tuesday, November 6th. Practice voting and see what happens! Text Y or N.',
    'prek-prevote': ('The PreK4SA election is tomorrow! '
        "Send us your zip code and we'll let you know where your closest polling place is.")
}

REPLIES = {
    "E": {
        "body": (
            "So glad to hear you're thinking about your student's future now! So are we! "
            "We're S2A, Spur to Action, aiming to inform you about the issues that are important to you. "
            "Look forward to hearing more about the latest education issue coming up in your area. "
            "Learn more about us at http://texasturnout.herokuapp.com. "
            "Reply STOP at any time, and we won't send you any more updates!"
        ),
        "media": []
    },
    "Y": {
        "body": (
            'Voting "yes" will increase funding so an additional 5,700 students can attend full-day Pre-K programs. '
            'The funding for this will be created by a small sales tax increase.\n\n'
            'Try "N" to see what the other side argues, or "MORE" for other info.'
        ),
        "media": []
    },
    "N": {
        "body": (
            'Voting "no" will maintain sales tax rates as they are (8.125%) '
            'and maintain the current figures of students attending Pre-K.\n\n'
            'Try "Y" to see what the other side argues, or "MORE" for other info.'
        ),
        "media": []
    },

    "T": {
        "body": (
            "So glad to hear you hate traffic! We do too!  We're S2A, Spur to Action, "
            'aiming to inform you about your local problems/issues. Look forward '
            'to hearing more the latest transportation issue coming up in your area. '
            'Learn more about us at http://texasturnout.herokuapp.com. '
            "Reply STOP at any time, and we won't send you any more updates."
        ),
        "media": []
    },
    "T-followup": {
        "body": 'Prop 1 is on Saturday, May 7. Practice voting and see what happens! Text YES or NO.',
        "media": [],
    },
    "YES": {
        "body": (
            'Voting "yes" on the proposition means standard background checks '
            'for these drivers will continue. Those checks do not include fingerprinting. '
            'The current regulations mandating criminal background check for '
            'ridesharing drivers would stay in place.\n\n'
            'Try "NO" to see what the other side argues, or "MORE" for other info.'
        ),
        "media": []
    },
    "NO": {
        "body": (
            'A vote of "no" means these drivers will be required to go through '
            'fingerprint background checks in addition to criminal background checks.\n\n'
            'Try "YES" to see what the other side argues, or "MORE" for other info.'
        ),
        "media": []
    },
    "MORE": {
        "body": 'Here is more info about local issues in San Antonio.',
        "media": ['http://i.giphy.com/3o6ozAxsUHHV2Kmy7m.gif']
    },
    "STOP": {
        "body": "Just kidding, you can't escape! Muhahahaha.",
        "media": []
    }
}

NAMES = {
    '+12036067072': 'Liam',
    '+15127367725': 'Lorena',
}
