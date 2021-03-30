from flask import Flask, json

class Webhook(object):
    
    def __init__(self, host, port):
        """ Constructor for Webhook tool """
        self.www = Flask(__name__)
        self.host = host
        self.port = port

    def start(self):
        """ Start the Web server for Webhooks """
        if self.www:
            self.www.run(host=self.host, port=self.port)

    def stop(self):
        """ Stop the Web server for Webhooks """
        if self.www:
            self.www.close()
