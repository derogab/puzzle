import json

from puzzle import Plugin
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

# Insert extra requirements for plugins in a requirements.txt file in the plugins folder
# Example: ./plugins/requirements.txt

class Example(Plugin):
    """ This plugin is just an example plugin """
    def __init__(self):
        super().__init__()
        self.description = 'Example plugin'

    def run(self):
        
        # Example of command in the telegram bot
        def hello(update: Update, context: CallbackContext) -> None:
            update.message.reply_text(f'Hello {update.effective_user.first_name}')

        self.tools.telegram.updater.dispatcher.add_handler(CommandHandler('hello', hello))

        # Example of a webhook 
        @self.tools.webhook.www.route('/example', methods=['GET'])
        def get_example():
            res = {
                "status": "success",
                "data": "example"
            }

            return json.dumps(res)
