# Xalabaias 🎉️ 

#### bot discord.py

qq eu descrevo nele?

# Documentação

## Comandos

#### xa!help ou xa!ajuda

Retorna uma embed com uma explicação de cada comando e como usá-lo.

#### xa!conversar

Inicia uma conversa com o Xalabaias (provavelmente você será xingado).

```apache
await msg.channel.send(chatbot.get_response(statement)) # statement é a mensagem do usuário e o chatbot gera uma resposta para essa mensagem.
```

Para parar, use o **xa!pararconversa.**

#### xa!pararconversa

Para a conversa com o Xalabaias.

#### xa!random [send/add]:

Aqui o primeiro comando que se "ramifica" em dois caminhos. O random é um comando de "troca de imagens" entre os usuários e  o xalagrabaias. Abaixo um pouco mais sobre:

##### send:

O Xalabaias envia uma foto **ALEATÓRIA** para o usuário no mesmo canal de texto que o comando foi enviado.

```apache
# dc = módulo do discord

fp = random.choice(randomImages) # escolhe aleatoriamente o caminho de uma imagem/vídeo
with open(fp, 'rb') as file: # abre esse caminho e lê em binário
    await msg.channel.send(file=dc.File(file)) # envia o arquivo
```

##### add [file]:

Esse comando é usado para adicionar ao banco de imagens do Xalabaias para ser enviado com o **xa!random send**.

```apache
for attach in msg.attachments: # cada anexo da mensagem
    if attach.content_type and attach.content_type.split('/')[0] in ['image', 'video']: # se o anexo é imagem ou vídeo:
        attach.save(os.path.join(dirassets, f'random/{attach.filename}')) # salva o anexo na pasta de assets
await msg.channel.send('Os arquivos foram salvos.')
```

O usuário, junto ao comando, deve anexar um ou mais arquivos (vídeo ou imagem).
