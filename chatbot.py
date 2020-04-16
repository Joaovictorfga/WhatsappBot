from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
    
    def tear_down(self):
        self.driver.quit()

    def send_message(self, contact, text):
        chat = self.driver.find_element_by_xpath(f"//span[@title='{contact}']")
        print('Nova mensagem :)')
        print(' ')
        time.sleep(2)
        chat.click()
        chat_box = self.driver.find_element_by_class_name('_1Plpp')
        print('Identificando usuário')
        print(' ')
        time.sleep(2)
        chat_box.click()
        chat_box.send_keys(text)
        send_button = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        print('Digitando bom dia')
        print(' ')
        time.sleep(2)
        send_button.click()
        print('Enviando')
        time.sleep(2)

    def check_last_message(self, contact):
        chat = self.driver.find_element_by_xpath(f"//span[@title='{contact}']")
        time.sleep(2)
        chat.click()
        list_of_messages = self.driver.find_elements_by_class_name('message-in')
        message1 = list_of_messages[len(list_of_messages)-1]
        box = message1.find_elements_by_class_name('_3FXB1')
        text_tag = box[len(box)-1].find_element_by_tag_name('span')
        text = text_tag.get_attribute('innerHTML')
        time.sleep(2)
        return text

    def initialize(self):
        print("Iniciando Inteligencia")
        self.driver.get('https://web.whatsapp.com')
        for i in range(15):
            print(f'{15 - i} segundos para confirmar o código QR...')
            time.sleep(1)
        print('Acesso permitido')
