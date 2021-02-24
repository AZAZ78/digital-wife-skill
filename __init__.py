from mycroft import MycroftSkill, intent_file_handler


class DigitalWife(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('wife.intent')
    def handle_wife_digital(self, message):
        self.speak_dialog('wife')


def create_skill():
    return DigitalWife()

