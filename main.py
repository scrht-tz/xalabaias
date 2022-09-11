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

r = list(os.listdir(os.path.join(dirassets, 'random')))
randomImages = []

for a in r:
    randomImages.append(os.path.join(dirassets, 'random')+'/'+a)


class Client(dc.Client):
    prefix = 'xa!'
    conversation = False

    async def on_ready(self):
        """Quando o bot estiver 'pronto'."""
        print(f'{str(self.user)} connected.')
        await self.change_presence(status=dc.Status.do_not_disturb)
    
    async def on_message(self, msg: dc.Message):
        statement = Statement(str(msg.content))
        if msg.content.startswith(f'{self.prefix}help') or msg.content.startswith(f'{self.prefix}ajuda'): # se é um comando de ajuda?
            embed=dc.Embed(title="Ajuda", description="Comandos e a descrição de cada um:", color=0xff0000)
            embed.add_field(name="xa!conversar", value="converse com o xalabaias", inline=False)
            embed.add_field(name="xa!random", value="add: adiciona os arquivos enviados\nsend: envia um arquivo aleatório", inline=True)
            embed.add_field(name="xa!pararconversa", value="para a conversa com o xalabaias", inline=True)
            embed.add_field(name="xa!help ou xa!ajuda", value="mostra os comandos", inline=True)
            embed.set_footer(text="tio zuca", icon_url='https://yt3.ggpht.com/SIDriJsk-Gmj0gJUq10Dq_xhOCswYhGc_Ay3Z8sB6nvasofz-vH7aROVSzuxxJMfLTiOi9s=s88-c-k-c0x00ffffff-no-rj-mo')
            await msg.channel.send(embed=embed)
        if msg.content.startswith(f'{self.prefix}pararconversa') and self.conversation: # se o comando é para parar a conversa
            self.conversation = False
        elif msg.content.startswith(f'{self.prefix}conversar') and not self.conversation: # se o comando é para começar a conversa
            self.conversation = True
            await msg.channel.send('começou...')
            await msg.channel.send(chatbot.get_response('a'))
        elif msg.content.startswith(f'{self.prefix}random send'): # se o comando é para mandar um arquivo aleatório
            with open(random.choice(randomImages), 'rb') as file:
                await msg.channel.send(file=dc.File(file))
        elif msg.content.startswith(f'{self.prefix}random add'): # se o comando é para adicionar um arquivo aleatório
            if not has_no_attachments(msg):
                for attach in msg.attachments:
                    if attach.content_type and attach.content_type.split('/')[0] in ['image', 'video']:
                        attach.save(os.path.join(dirassets, f'random/{attach.filename}'))
                await msg.channel.send('Os arquivos foram salvos.')
            else:
                await msg.channel.send('Cabeça de bagre! Envia uma imagem ou um vídeo pra eu salvar! tmnc...')
        if self.conversation and not msg.content.startswith(self.prefix):
            await msg.channel.send(chatbot.get_response(statement))


def has_no_attachments(msg: dc.Message):
    return len(msg.attachments) == 0

if __name__ == '__main__':
    client = Client()

    asyncio.run(client.login(get_token()))

