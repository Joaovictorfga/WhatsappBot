from chatbot import WhatsappBot
import time

print('Inicializando instâncias..')
bot = WhatsappBot()
bot.initialize()
time.sleep(1)
contact = 'Bot do bom dia'
last_message = bot.check_last_message(contact)
while True:
    checked_message = bot.check_last_message(contact)
    if last_message != checked_message:
        if checked_message == 'Bom dia':
            bot.send_message(contact, 'Bom dia!')
        if checked_message == 'Boa noite':
            bot.send_message(contact,'Bom noite!')
        last_message = checked_message
    else:
        print('Nenhuma nova mensagem :(')
        print(' ')
    time.sleep(2)     
