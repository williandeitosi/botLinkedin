import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from dotenv import load_dotenv

load_dotenv()
linkedin_email = os.getenv("LINKEDIN_EMAIL")
linkedin_password = os.getenv("LINKEDIN_PASSWORD")

driver = webdriver.Chrome()
driver.maximize_window()

access = [linkedin_email, linkedin_password, "backend"]
driver.get("https://www.linkedin.com")
sleep(5)
email = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/a')
email.click()
sleep(2)
putEmail = driver.find_element(By.XPATH, '//*[@id="username"]')
putEmail.send_keys(access[0])


sleep(1)
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.click()
password.send_keys(access[1])

sleep(0.5)
enter = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
enter.click()

sleep(5)

# input("")
pesquisar = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
pesquisar.click()
pesquisar.send_keys(access[2])
pesquisar.send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 10)
wait.until(
    EC.presence_of_element_located((By.XPATH, '//button[@aria-pressed="false"]'))
)

buttons = driver.find_elements(By.XPATH, '//button[@aria-pressed="false"]')
for btn in buttons:
    if btn.text == "Pessoas":
        btn.click()
        sleep(5)

        i = 1
        while True:
            try:
                if i >= 10:
                    i = 1
                    driver.execute_script("window.scroll(0, 9999)")
                    avancar = driver.find_element(
                        By.XPATH, '//*[@aria-label="Avançar"]'
                    )
                    avancar.click()
                conectar = driver.find_elements(
                    By.XPATH,
                    '//button[@class="artdeco-button artdeco-button--2 artdeco-button--secondary ember-view"]',
                )
                for conect in conectar:
                    i += 1
                    if conect.text == "Conectar":
                        conect.click()
                        sleep(1)
                        nome_pessoa = driver.find_element(
                            By.XPATH,
                            '//div[@class="artdeco-modal__content ember-view"]',
                        )
                        strong = nome_pessoa.find_element(By.XPATH, ".//strong")
                        nome = strong.text

                        sleep(1)

                        adicionar_nota = driver.find_element(
                            By.XPATH, '//button[@aria-label="Enviar sem nota"]'
                        )
                        adicionar_nota.click()

                        # sleep(1)

                        # mensagem = f"Olá {nome}, como vai? Estou buscando oportunidade na área de programação, estou usando um RPA para me comunicar com você que eu mesmo desenvolvi, adoraria fazer parte da sua rede. Podemos conversar?"
                        # textarea = driver.find_element(
                        #     By.XPATH, '//textarea[@name="message"]'
                        # )
                        # textarea.click()
                        # textarea.send_keys(mensagem)

                        # sleep(1)

                        # enviar = driver.find_element(
                        #     By.XPATH, '//button[@aria-label="Enviar agora"]'
                        # )
                        # enviar.click()
            except:
                print("[ERRO]")

driver.quit()
# TODO: Melhorar o bot de conexoes, ele execulta normalmente , porem ainda da muitos erros e preciso de alguns if
