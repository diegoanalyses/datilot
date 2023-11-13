from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# ^ ------------------------------------------------------------
URL = "https://conatjuris.sefaz.ce.gov.br/#/"
driver = webdriver.Firefox()
driver.get(URL)
elem = driver.find_element
elems = driver.find_elements
# ^ ------------------------------------------------------------
sua_busca = elem(By.XPATH, "//input[@placeholder='Informe aqui sua busca']")
botao_busca = elem(By.XPATH,
                   "//button[@class='btn btn-primary btn-lg m-l-5 waves-effect']//i[@class='pi pi-search']")
de_ano = elem(By.XPATH, "//input[@id='mat-input-0']")
ate_ano = elem(By.XPATH, "//input[@id='mat-input-1']")
resolucao = elem(By.XPATH, "//input[@id='mat-input-2']")
proc = elem(By.XPATH, "//input[@name='numeroProcesso']")
de_julg = elem(By.XPATH, "//input[@id='mat-input-3']")
ate_julg = elem(By.XPATH, "//input[@id='mat-input-4']")
auto = elem(By.XPATH, "//input[@id='mat-input-5']")
relator = elem(By.XPATH, "//input[@name='relator']")
# ^ ------------------------------------------------------------
sua_busca.send_keys('icms')
botao_busca.click()
# ^ ---------
divs = elems(By.TAG_NAME, 'div')

for idx, div in enumerate(divs):
    div_und = div.find_elements(By.TAG_NAME, 'div')

    print(idx, len(div_und))

