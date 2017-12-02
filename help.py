
# -*- coding: utf-8 -*-
from chatterbot import ChatBot

#import logging
#logging.basicConfig(level=logging.INFO)
bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="../database.db"
    'Example Bot',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'

)
bot.train(
    'chatterbot.corpus.english.help'

)

print("So you want to know about me? Come on don't be shy ask me it out")

while True:
    try:
        bot_input = bot.get_response(None)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break



