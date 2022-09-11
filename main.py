import key
import os
import random
from spacy.cli import download
import discord
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

download('en_core_web_sm')


class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


chatbot = ChatBot('chatbot', tagger_language=ENGSM)

lista = ['vai tomar no cu']

trainer = ListTrainer(chatbot)

trainer.train(lista)


class Client(discord.Client):
    async def on_ready(self):
        print(f'{str(self.user)}')
    
    async def on_message(self, msg: discord.Message):
        await msg.channel.send(msg)


if __name__ == '__main__':
    client = Client()

    client.login(key.get_token())

