from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://web.whatsapp.com/') #abre o site Whatsapp Web
time.sleep(15) #da um sleep de 15 segundos, tempo para scannear o QRCODE

contatos = ['Contato']
mensagem = 'fala maluko'    #Mensagens

#Midia = (trava ZAP) (caminho do arquivo com barra invertida / ) 
#midia = "/home/pinheirocfc/Imagens/bom-dia.jpg"
   
#pesquisa o Contato/Grupo
def buscar_contato(contatos):
    campo_pesquisa = driver.find_element('xpath','//p[contains(@class,"selectable-text copyable-text")]')
    time.sleep(1)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contatos)
    campo_pesquisa.send_keys(Keys.ENTER)

#envia a mensagem
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements('xpath','//p[contains(@class,"selectable-text copyable-text")]')
    campo_mensagem[1].click()
    time.sleep(1)
    campo_mensagem[1].send_keys(str(mensagem))
    campo_mensagem[1].send_keys(Keys.ENTER)

#envia imagens ==> desabilitado, por enquanto
# def enviar_midia(midia):
#     driver.find_element_by_css_selector("span[data-icon='clip']").click()
#     attach = driver.find_element_by_css_selector("input[type='file']")
#     attach.send_keys(midia)
#     time.sleep(3)
#     send = driver.find_element_by_css_selector("span[data-icon='send']")
#     send.click()    

while True:
    for contatos in contatos:
        buscar_contato(contatos)
        enviar_mensagem(mensagem)     # Deixe comentado a função de repetição while true para mandar apenas uma mensagem
        # enviar_midia(midia) 
        time.sleep(1)