from telegram.ext import Updater

class Telegram(object):
    
    def __init__(self, token):
        """ Constructor for Telegram tool """
        self.updater = Updater(token)

    def start(self):
        """ Start the telegram bot """
        if self.updater:
            self.updater.start_polling()

    def start_and_idle(self):
        """ Start (and idle) the telegram bot """
        if self.updater:
            self.updater.start_polling()
            self.updater.idle()

    def stop(self):
        """ Stop the telegram bot """
        if self.updater:
            self.updater.stop()
        