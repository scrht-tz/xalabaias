from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from chatterbot.conversation import Statement
from spacy.cli import download

download('pt_core_news_sm')
class ENGSM:
    ISO_639_1 = 'pt_core_news_sm'

chatbot = ChatBot('chatbot', tagger_language=ENGSM)

lista = ['vai tomar no cu', 'tu quica',
        'vai pra casa do caralho', 'alienigena uououuo',
        'vai mamar', 'vo nao',
        'vai sentar vai', 'tu que senta na piip',
        'vai ter que sair do armário hein!', 'já tô fora!',
        'Por favor, pare de mostrar seu orifício anal!', 'nunca!',
        'O Xabagraia aqui adora cuzcuz.', 'cuzcuz meu krl', 
        'Caralho!', 'pqp']

trainer = ListTrainer(chatbot)

trainer.train(lista)


if __name__ == '__main__':
    info = 3
    while not info in [0, 1]:
        info = int(input('Receber informações sobre o chatbot? [0/1]: '))
    while True:
        msg = str(input('user [^X exit]: '))
        if msg == '\x18':
            break
        reply = chatbot.get_response(msg)
        if isinstance(reply, Statement):
            if info == 0:
                print(f'bot: {reply}')
            elif info == 1:
                print(f'bot [{reply.confidence}]: {reply}')