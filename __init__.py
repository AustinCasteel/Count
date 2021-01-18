# -*- coding: utf-8 -*-
from naomi import plugin
from naomi import profile
import os
os.environ['w2n.lang']=profile.get(['language'])
from word2numberi18n import w2n

class Count(plugin.SpeechHandlerPlugin):
    def intents(self):
        return {
            'CountIntent': {
                'locale': {
                    'en-US': {
                        'keywords': {
                            'NumberKeyword': w2n.filebased_number_system.keys()
                        },
                        'templates': [
                            'COUNT TO {NumberKeyword}',
                            'COUNT FROM {NumberKeyword}'
                        ]
                    }
                },
                'action': self.handle
            }
        }

    @staticmethod
    def word2number(intent):
        number = None
        if "matches" in intent:
            if "NumberKeyword" in intent["matches"]:
                number = w2n.word_to_num(" ".join(intent['matches']['NumberKeyword']))
        return number

    def handle(self, intent, mic):
        preprocess = intent['input'].split()
        if "TO" in preprocess:
            number = self.word2number(intent)
            if isinstance(number, int):
                for i in range(1, number+1, +1):
                    mic.say(str(i))
            else:
                mic.say("I'm sorry, I did not hear a number")
        elif "FROM" in preprocess:
            number = self.word2number(intent)
            if isinstance(number, int):
                for i in range(number, 0, -1):
                    mic.say(str(i))
            else:
                mic.say("I'm sorry, I did not hear a number")
