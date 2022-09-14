from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time, json

driver = Chrome()

with Chrome() as driver:
    driver.get("http://moodlep.uem.br/")

    #login no Moodlep
    textbox_ra = driver.find_element('xpath','//*[@id="login_username"]')
    textbox_ra.send_keys('ra120122')

    textbox_password = driver.find_element('xpath','//*[@id="login_password"]')
    textbox_password.send_keys('46f6d242')

    botao = driver.find_element('xpath','//*[@id="login"]/div[4]/input')
    botao.click()
    
    time.sleep(4)

    driver.get('https://moodlep.uem.br/message/index.php?user=26377&id=30983')

    time.sleep(4)

    mensagem_moodlep = driver.find_element('xpath','//*[@id="region-main"]/div/div/div/div[2]/div[3]/div[1]/div[1]/textarea')
    botao_fofo = driver.find_element('xpath', '//button[text()="Enviar"]')

    for i in range(50):
        mensagem_moodlep.send_keys('É Vinicius Okagawa ou Okaguiwa? A oferta de lavar o rosto ainda está de pé !!')
        botao_fofo.click() 
        time.sleep(2)
    time.sleep(100)
