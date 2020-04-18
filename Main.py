import random
from notion.client import NotionClient
import re


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class NotionAPI():

    random_number = -1
    origin_word=''
    list_translated_words=[]

    client = NotionClient(
        token_v2="Your notion token")
    cv = client.get_collection_view(
        "Your website link")

    def parse_data(self,s):
            result = re.split(r'ー', s)
            return result

    def write_data(self, result):
        row = self.cv.collection.add_row()
        row.name, row.estimated_value = result
        result = self.cv.default_query().execute()

    #Read all data
    def read_data(self):
        for row in self.cv.collection.get_rows():
            print("{} - {}".format(row.name, row.estimated_value))




def start(update, context):
    update.message.reply_text('Hi!')

def help(update, context):
    update.message.reply_text('Help!')

def echo(update, context):
    example = update.message.text
    if example.count('ー') == 1:
        notion.write_data(notion.parse_data(example))
        update.message.reply_text('Done it ')
    else:
        update.message.reply_text("Not right format ")

def main():

    updater = Updater("Your telegram token", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    notion = NotionAPI()
    main()






