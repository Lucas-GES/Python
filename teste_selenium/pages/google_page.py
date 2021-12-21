from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser

class GooglePageLocator(object):
    
       INPUT_PESQUISA =  '[name="q"]'
       BUTTON_PESQUISA = '.gNO89b'
       BUTTON_ESTOU_COM_SORTE = '[name="btnI"]'
       BUTTON_NUMERO2 = '[jsname="lVjWed"]'
       BUTTON_MULTIPLICAR = '[jsname="YovRWb"]'
       BUTTON_NUMERO1 = '[jsname="N10B9"]'
       BUTTON_NUMERO0 = '[jsname="bkEvMb"]'
       BUTTON_IGUAL = '[jsname="Pt8tGc"]'

class GooglePage(Browser):
    def get_element(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, locator)))
        
        return self.driver.find_element(By.CSS_SELECTOR, locator)
    
    def acess_page(self, url):
        
        self.driver.get(url)
        
    def send_keys_input_pesquisa(self):
        input_titulo = self.get_element(GooglePageLocator.INPUT_PESQUISA)
        input_titulo.send_keys('calculadora')
        
    def barrel_roll_input_pesquisa(self):
        input_titulo = self.get_element(GooglePageLocator.INPUT_PESQUISA)
        input_titulo.send_keys('do a barrel roll') 
        
    def google_gravity_input_pesquisa(self):
        input_titulo = self.get_element(GooglePageLocator.INPUT_PESQUISA)
        input_titulo.send_keys('Google Gravity') 
        
    def click_button_pesquisa(self):
        button = self.get_element(GooglePageLocator.BUTTON_PESQUISA)
        button.click()
        
    def click_button_estou_com_sorte(self):
        button = self.get_element(GooglePageLocator.BUTTON_ESTOU_COM_SORTE)
        button.click()
        
    def click_button_numero2(self):
        button = self.get_element(GooglePageLocator.BUTTON_NUMERO2)
        button.click()
        
    def click_button_multiplicar(self):
        button = self.get_element(GooglePageLocator.BUTTON_MULTIPLICAR)
        button.click()
        
    def click_button_numero1(self):
        button = self.get_element(GooglePageLocator.BUTTON_NUMERO1)
        button.click()  
        
    def click_button_numero0(self):
        button = self.get_element(GooglePageLocator.BUTTON_NUMERO0)
        button.click()  
        
    def click_button_igual(self):
        button = self.get_element(GooglePageLocator.BUTTON_IGUAL)
        button.click()        