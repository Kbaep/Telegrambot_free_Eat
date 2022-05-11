import logging
import telegram
import os
import dotenv
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from googlemaps import Client as GoogleMaps

dotenv.load_dotenv('.env')

# Включить ведение журнала
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

LOCATION, PHOTO, DIET, SERVINGS, TIME, CONFIRMATION = range(6)

reply_keyboard = [['Confirm', 'Restart']]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
TOKEN = 'YOURTELEGRAMBOTTOKEN'
bot = telegram.Bot(token=TOKEN)
chat_id = 'YOURTELEGRAMCHANNEL'
GMAPSAPI = 'YOURGOOGLEMAPSAPITOKEN'
gmaps = GoogleMaps(GMAPSAPI)

PORT = int(os.environ.get('PORT', 5000))



if __name__ == '__main__':
    main()