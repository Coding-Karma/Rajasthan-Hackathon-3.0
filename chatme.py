
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
#import logging
#logging.basicConfig(level=logging.INFO)
bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="../databaseme.db"
    'Example Bot',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
bot.train(
    'chatterbot.corpus.english'

)

print("Type something to begin...")

while True:
    try:
        bot_input = bot.get_response(None)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break



