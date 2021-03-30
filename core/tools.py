from .telegram import Telegram
from .webhook import Webhook

class Tools(object):
    
    def __init__(self):
        """ Constructor for Tools object """
        self.webhook = None
        self.telegram = None

    def set_telegram(self, token):
        """ Init telegram bot updater """
        if token:
            self.telegram = Telegram(token)

    def set_webhook(self, host, port):
        """ Init web server for webhooks """
        if host and port:
            self.webhook = Webhook(host, port)
