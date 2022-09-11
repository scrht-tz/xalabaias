from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
from spacy.cli import download

import logging

#download('en_core_web_sm')
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

logging.basicConfig(level=logging.INFO)


chatbot = ChatBot('chatbot', tagger_language=ENGSM)

lista = ['vai tomar no cu']

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.portuguese')


if __name__ == '__main__':
    while True:
        msg = str(input('user [^X exit]: '))
        if msg == '\x18':
            break
        reply = chatbot.generate_response(Statement(msg))
        print(f'bot: {reply.text}')