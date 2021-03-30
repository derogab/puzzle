""" Main application """

import os

from dotenv import load_dotenv
from jarvis import PluginCollection
from jarvis import Tools

# Load .env file
load_dotenv()

# Init main function
def main():
    """ main function that runs the application """

    # Create tools
    tools = Tools()

    # Init telegram
    tools.set_telegram(os.getenv('TELEGRAM_TOKEN') or None)

    # Init webhook
    www_host = os.getenv('WEBHOOK_HOST') or '0.0.0.0'
    www_port = os.getenv('WEBHOOK_PORT') or '8080'
    tools.set_webhook(www_host, www_port)

    # Link all plugins 
    my_plugins = PluginCollection('plugins', tools)
    my_plugins.start_all_plugins()

    # Start telegram bot 
    tools.telegram.start()

    # Start webserver 
    tools.webhook.start()

# Start main function
if __name__ == '__main__':
    main()
