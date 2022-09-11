"""Xalabaias"""

from tokenbot import get_token
from chatbot import chatbot
from chatterbot.conversation import Statement
import os
import asyncio
import random
import discord as dc

class Client(dc.Client):
    prefix = '$'
    conversation = False
    async def on_ready(self):
        """Quando o bot estiver 'pronto'."""
        print(f'{str(self.user)} connected.')
        await self.change_presence(status=dc.Status.do_not_disturb)
    
    async def on_message(self, msg: dc.Message):
        statement = Statement(str(msg.content))
        if msg.content.startswith(f'{self.prefix}conversar'):
            self.conversation = True
        if self.conversation and not msg.content.startswith(self.prefix):
            await msg.channel.send(chatbot.generate_response(statement))


if __name__ == '__main__':
    client = Client()

    asyncio.run(client.login(get_token()))

