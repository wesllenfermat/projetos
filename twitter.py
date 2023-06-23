from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
from selenium.webdriver.common.keys import Keys

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1440,900', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver
def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)

driver = iniciar_driver()
driver.get('https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoicHQifQ%3D%3D%22%7D')
sleep(5)
login = driver.find_element(By.XPATH, '//input[@autocomplete="username"]')
driver.execute_script('arguments[0].click()', login)
usuario = """@Usuario"""
digitar_naturalmente(usuario,login)
login.send_keys(Keys.ENTER)
sleep(1)
senha = driver.find_element(By.XPATH, '//input[@name="password"]')
driver.execute_script('arguments[0].click()', senha)
texto_2="""Senha123"""
digitar_naturalmente(texto_2,senha)
sleep(1)
senha.send_keys(Keys.ENTER)
sleep(2)
acontecendo = driver.find_element(By.XPATH, '//div[@role="textbox"]')
driver.execute_script('arguments[0].click()', acontecendo)
sleep(1)
tweetar="""Mensagem"""
digitar_naturalmente(tweetar,acontecendo)
sleep(1)
publicar = driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
driver.execute_script('arguments[0].click()', publicar)

input('')
driver.close()
