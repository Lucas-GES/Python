from selenium import webdriver

navegador = webdriver.Chrome()

navegador.get("https://ri.magazineluiza.com.br/")
navegador.find_element_by_xpath('//*[@id="banner"]/a[1]/img').click()
navegador.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/a[1]/span').click()

driver = webdriver.Chrome()  # Inicia o browser
driver.get('https://www.python.org/')  # Acessar a URL especificada
driver.find_element_by_css_selector('#id-search-field').send_keys("python")  # Digita o texto "python" no input
driver.find_element_by_css_selector('#submit').click()  # Clica no botão de submit
driver.quit()