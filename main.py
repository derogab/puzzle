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

    # Link all plugins 
    my_plugins = PluginCollection('plugins', tools)
    my_plugins.start_all_plugins()

    # Start telegram bot 
    tools.telegram.start_polling()
    tools.telegram.idle()

# Start main function
if __name__ == '__main__':
    main()
