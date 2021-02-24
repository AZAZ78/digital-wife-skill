from mycroft import MycroftSkill, intent_file_handler


class DigitalWife(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('wife.digital.intent')
    def handle_wife_digital(self, message):
        self.speak_dialog('wife.digital')


def create_skill():
    return DigitalWife()

