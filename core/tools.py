from .telegram import Telegram

class Tools(object):
    
    def __init__(self):
        """ Constructor for Tools object """
        self.telegram = None

    def set_telegram(self, token):
        """ Init telegram bot updater """
        if token:
            self.telegram = Telegram(token)
