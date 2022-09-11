"""Xalabaias"""

from tokenbot import get_token
from chatbot import chatbot
from chatterbot.conversation import Statement
import os
import asyncio
import random
import discord as dc

dirprin = os.path.dirname(__file__)
dirassets = os.path.join(dirprin, 'assets')

randomImages = list(os.listdir(os.path.join(dirassets, 'random')))

class Client(dc.Client):
    prefix = 'xa!'
    conversation = False
    occurences = [['help', 'ajuda'], ['conversar', 'pararconversa'], ['random send', 'random add']]
    async def on_ready(self):
        """Quando o bot estiver 'pronto'."""
        print(f'{str(self.user)} connected.')
        await self.change_presence(status=dc.Status.do_not_disturb)
    
    async def on_message(self, msg: dc.Message):
        statement = Statement(str(msg.content))
        if msg.content.startswith(f'{self.prefix}help') or msg.content.startswith(f'{self.prefix}ajuda'):
            embed=dc.Embed(title="Ajuda", description="Comandos e a descrição de cada um:", color=0xff0000)
            embed.add_field(name="xa!conversar", value="converse com o xalabaias", inline=False)
            embed.add_field(name="xa!random", value="add: adiciona os arquivos enviados\nsend: envia um arquivo aleatório", inline=True)
            embed.add_field(name="xa!pararconversa", value="para a conversa com o xalabaias", inline=True)
            embed.add_field(name="xa!help ou xa!ajuda", value="mostra os comandos", inline=True)
            embed.set_footer(text="tio zuca", icon_url='https://yt3.ggpht.com/SIDriJsk-Gmj0gJUq10Dq_xhOCswYhGc_Ay3Z8sB6nvasofz-vH7aROVSzuxxJMfLTiOi9s=s88-c-k-c0x00ffffff-no-rj-mo')
            await msg.channel.send(embed=embed)
        if msg.content.startswith(f'{self.prefix}pararconversa') and self.conversation:
            self.conversation = False
        elif msg.content.startswith(f'{self.prefix}conversar') and not self.conversation:
            self.conversation = True
        elif msg.content.startswith(f'{self.prefix}random send'):
            with open(random.choice(randomImages), 'rb') as file:
                await msg.channel.send(file=dc.File(file))
        elif msg.content.startswith(f'{self.prefix}random add'):
            if not has_no_attachments(msg):
                for attach in msg.attachments:
                    if attach.content_type and attach.content_type.split('/')[0] in ['image', 'video']:
                        attach.save(os.path.join(dirassets, f'random/{attach.filename}'))
                await msg.channel.send('Os arquivos foram salvos.')
        if self.conversation and not msg.content.startswith(self.prefix):
            await msg.channel.send(chatbot.generate_response(statement))


def has_no_attachments(msg: dc.Message):
    return len(msg.attachments) == 0

if __name__ == '__main__':
    client = Client()

    asyncio.run(client.login(get_token()))

