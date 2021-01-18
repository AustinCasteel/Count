# -*- coding: utf-8 -*-
from naomi import plugin

class Count(plugin.SpeechHandlerPlugin):
    def intents(self):
        return {
            'CountIntent': {
                'locale': {
                    'en-US': {
                        'templates': [
                            'COUNT TO {Query}',
                            'COUNT FROM {Query}'
                        ]
                    }
                },
                'action': self.handle
            }
        }

    def handle(self, intent, mic):
        text = intent['input']

        if text.startswith( 'COUNT TO' )
            preprocess = text.split()
            number = preprocess [-1]
            for i in range(1, number+1, +1):
                mic.say(str(i))

        if text.startswith( 'COUNT FROM' )
            preprocess = text.split()
            number = preprocess [-1]
            for i in range(number, 0, -1):
                mic.say(str(i))