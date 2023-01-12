from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    
    __login_page = {'by':By.ID, 'locator':'account-login'}
    __customer_titulo = {'by':By.XPATH, 'locator':'//div[@class="well"]//h2[text()="Returning Customer"]'}
    __email_box = {'by':By.XPATH, 'locator':'//input[@name = "email"]'}
    __password_box = {'by':By.XPATH, 'locator':'//input[@name = "password"]'}
    __login_button = {'by':By.XPATH, 'locator':'//input[@type="submit"]'}
    __confirmation_text = {'by':By.XPATH,'locator':'//div[@class= "alert alert-danger alert-dismissible"]'}

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.__verificar_pagina_login()

    def __verificar_pagina_login(self):
        login_page = self._get_element(self.__login_page['by'],self.__login_page['locator'])
        self._is_present(login_page,'No se encuentra la pagina de login')
        self._is_visible(login_page,'La pagina de login no se encuentra visible')

    def verificar_titulo_returning_customer(self):
        img_element = self._get_element(self.__customer_titulo['by'],self.__customer_titulo['locator'])
        self._is_present(img_element,'No se encuentra el titulo Returning Customer')
        self._is_visible(img_element,'El titulo Returning Customer no se encuentra visible')

    def ingresar_email(self,text):
        input_email = self._get_element(self.__email_box['by'],self.__email_box['locator'])
        self._is_present(input_email,'No se encuentra el input del Email')
        self._is_visible(input_email,'El input del Email no se encuentra visible')
        self._write(input_email,text)

    def ingresar_password(self,text):
        input_password = self._get_element(self.__password_box['by'],self.__password_box['locator'])
        self._is_present(input_password,'No se encuentra el input de Password')
        self._is_visible(input_password,'El input de Password no se encuentra visible')
        self._write(input_password,text)

    def click_login(self):
        continue_element = self._get_element(self.__login_button['by'], self.__login_button['locator'])
        self._is_present(continue_element, 'No se encuentra el boton de Login')
        self._is_visible(continue_element, 'El boton de Login no se encuentra visible') 
        self._is_enabled(continue_element, 'El boton de Login Policy no se encuentra habilitado') 
        self._click(continue_element)
    
    def verificar_confirmacion_login(self,text_expected):
        text_confirmation_element = self._get_element(self.__confirmation_text['by'],self.__confirmation_text['locator'])
        self._is_present(text_confirmation_element,'No se encuentra el texto de la confirmacion de login')
        self._is_visible(text_confirmation_element,'El texto de la confirmacion no encontrado no se encuentra visible')
        actual_text = self._get_text(text_confirmation_element)
        assert text_expected == actual_text , f'El mensaje de l confirmacion, no coincide. Se esperaba "{text_expected}" y se obtuvo "{actual_text}"'
