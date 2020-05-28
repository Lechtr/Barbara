from mycroft import MycroftSkill, intent_file_handler
from mycroft.audio import wait_while_speaking
from mycroft.skills.context import *
from mycroft.util.log import LOG

from datetime import date

# TODO: Fallback Skill einrichten

class BarbaraSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        # Aufstellungsdatum, für die Altersberechnung
        self.initial_date = date(2020, 5, 28)

    def initialize(self):
        # Word entity ist Platzhalter für beliebieges Wort
        self.register_entity_file("word.entity")
        # self.parser = WiktionaryParser()


    ### normale Frage-Antwort-Intents ###

    @intent_file_handler('barbara.what.is.name.intent')
    def handle_barbara_name(self, message):
        self.speak_dialog('barbara.name.introduction')

    @intent_file_handler('barbara.how.are.you.intent')
    def handle_barbara_how_are_you(self, message):
        self.speak_dialog('barbara.I.feel.fine')

    @intent_file_handler('barbara.who.are.you.intent')
    def handle_barbara_who_are_you(self, message):
        self.speak_dialog('barbara.I.am')

    @intent_file_handler('barbara.why.are.you.here.intent')
    def handle_barbara_why_are_you_here(self, message):
        self.speak_dialog('barbara.I.am.here.because')



    ### komplexere Intents ###
    @intent_file_handler('barbara.how.old.are.you.intent')
    def handle_barbara_how_old(self, message):
        age = date.today() - self.initial_date
        self.speak_dialog('barbara.I.am.old', {'age': age.days})

    # TODO: hier ask_yesno prüfen obs funktioniert
    @intent_file_handler('barbara.what.can.you.do.intent')
    def handle_barbara_what_can_you_do(self, message):
        # Fragen ob Beispielfragen gegeben werden sollen
        give_examples = self.ask_yesno('barbara.ask.example.questions')

        # Falls ja
        if give_examples == "yes":
            self.speak_dialog('barbara.example.questions')
        # Falls Nein
        else:
            # Anders weiterhelfen?
            # Ja
            if self.ask_yesno('barbara.ask.can.I.help.otherwise') == "yes":
                # TODO: hier als Prompt implementieren
                self.speak_dialog('barbara.ask.what.dou.you.want.to.know')
            # Nein
            else:
                self.speak_dialog('barbara.goodbye')










    # @intent_file_handler('fallback.wiktionary.definition.intent')
    # def handle_wiktionary_definition(self, message):
        # #Get word to define from utterance
        # word = message.data.get('word')
        # #Lookup the word using Wiktionary
        # get_word_info = self.parser.fetch(word)

        # #Speak definition for requested word back to user
        # try:
            # # Get first definition from wiktionary response
            # response = get_word_info[0]['definitions'][0]['text'][1]
            # # Log the definition
            # LOG.info(response)
            # self.speak_dialog('fallback.wiktionary', {'word': word, 'definition': response})
        # except:
            # self.speak_dialog('error.wiktionary')


    def stop(self):
        pass


def create_skill():
    return BarbaraSkill()

