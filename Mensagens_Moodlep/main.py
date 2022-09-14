from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time, json

driver = Chrome()

with Chrome() as driver:
    #abrindo o site do moodlep
    driver.get("http://moodlep.uem.br/")
    
    #login no Moodlep
    ra = 'ra'
    password = 'password'
    link_do_chat_do_amiguinho = 'link'

    textbox_ra = driver.find_element('xpath','//*[@id="login_username"]')
    textbox_ra.send_keys(ra)

    textbox_password = driver.find_element('xpath','//*[@id="login_password"]')
    textbox_password.send_keys(password)

    botao = driver.find_element('xpath','//*[@id="login"]/div[4]/input')
    botao.click()
    
    time.sleep(4)

    #abrindo o chat
    driver.get(link_do_chat_do_amiguinho)

    time.sleep(4)
    #Hora de enviar as mensagens !!
    mensagem_moodlep = driver.find_element('xpath','//*[@id="region-main"]/div/div/div/div[2]/div[3]/div[1]/div[1]/textarea')
    botao_fofo = driver.find_element('xpath', '//button[text()="Enviar"]')

    for i in range(50):
        mensagem_moodlep.send_keys('CÁSSIOOOOOOOOOOOO !!!!! :D')
        botao_fofo.click() 
        time.sleep(2)
    time.sleep(100)
