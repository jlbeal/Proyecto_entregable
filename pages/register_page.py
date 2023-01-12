from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):
    
    __register_page = {'by':By.ID, 'locator':'content'}
    __register_titulo = {'by':By.XPATH, 'locator':'//div[@id="content"]//h1'}
    __first_name_box = {'by':By.NAME, 'locator':'firstname'}
    __last_name_box = {'by':By.NAME, 'locator':'lastname'}
    __email_box = {'by':By.NAME, 'locator':'email'}
    __telephone_box = {'by':By.NAME, 'locator':'telephone'}
    __password_box = {'by':By.NAME, 'locator':'password'}
    __confirm_password_box = {'by':By.NAME, 'locator':'confirm'}
    __privacy_checkbox = {'by':By.NAME, 'locator':'agree'}
    __continue_button = {'by':By.XPATH, 'locator':'//input[@type="submit"]'}
    __text_confirmation = {'by':By.XPATH,'locator':'//div[@class= "alert alert-danger alert-dismissible"]'}

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.__verificar_pagina_register()

    def __verificar_pagina_register(self):
        register_page = self._get_element(self.__register_page['by'],self.__register_page['locator'])
        self._is_present(register_page,'No se encuentra la pagina de Register')
        self._is_visible(register_page,'La pagina de Register no se encuentra visible')

    def verificar_titulo_register_customer(self):
        titulo_register = self._get_element(self.__register_titulo['by'],self.__register_titulo['locator'])
        self._is_present(titulo_register,'No se encuentra el titulo de Register Customer')
        self._is_visible(titulo_register,'El titulo de Register Customer no se encuentra visible')

    def ingresar_first_name(self,text):
        input_first_name = self._get_element(self.__first_name_box['by'],self.__first_name_box['locator'])
        self._is_present(input_first_name,'No se encuentra el input de First Name')
        self._is_visible(input_first_name,'El input de First Name no se encuentra visible')
        self._write(input_first_name,text)

    def ingresar_last_name(self,text):
        input_last_name = self._get_element(self.__last_name_box['by'],self.__last_name_box['locator'])
        self._is_present(input_last_name,'No se encuentra el input de Last Name')
        self._is_visible(input_last_name,'El input de Last Name no se encuentra visible')
        self._write(input_last_name,text)

    def ingresar_email(self,text):
        input_email = self._get_element(self.__email_box['by'],self.__email_box['locator'])
        self._is_present(input_email,'No se encuentra el input del Email')
        self._is_visible(input_email,'El input del Email no se encuentra visible')
        self._write(input_email,text)

    def ingresar_telephone(self,text):
        input_telephone = self._get_element(self.__telephone_box['by'],self.__telephone_box['locator'])
        self._is_present(input_telephone,'No se encuentra el input de Telephone')
        self._is_visible(input_telephone,'El input de Telephone no se encuentra visible')
        self._write(input_telephone,text)

    def ingresar_password(self,text):
        input_password = self._get_element(self.__password_box['by'],self.__password_box['locator'])
        self._is_present(input_password, 'No se encuentra el input de Password')
        self._is_visible(input_password,'El input de Password no se encuentra visible')
        self._write(input_password,text)
    
    def ingresar_confirm_password(self,text):
        input_confirm_password = self._get_element(self.__confirm_password_box['by'],self.__confirm_password_box['locator'])
        self._is_present(input_confirm_password, 'No se encuentra el input de Password Confirm')
        self._is_visible(input_confirm_password,'El input de Password Confirm no se encuentra visible')
        self._write(input_confirm_password,text)

    def click_privacy_policy(self):
        privacy_element = self._get_element(self.__privacy_checkbox['by'], self.__privacy_checkbox['locator'])
        self._is_present(privacy_element, 'No se encuentra el checkbox Privacy Policy')
        self._is_visible(privacy_element, 'El checkbox Privacy Policy no se encuentra visible') 
        self._is_enabled(privacy_element, 'El checkbox Privacy Policy no se encuentra habilitado') 
        self._click(privacy_element)

    def click_continue(self):
        continue_element = self._get_element(self.__continue_button['by'], self.__continue_button['locator'])
        self._is_present(continue_element, 'No se encuentra el boton de Continue')
        self._is_visible(continue_element, 'El boton de Continue no se encuentra visible') 
        self._is_enabled(continue_element, 'El boton de Continue no se encuentra habilitado') 
        self._click(continue_element)
    
    def verificar_confirmacion(self,text_expected):
        text_confirmation_element = self._get_element(self.__text_confirmation['by'],self.__text_confirmation['locator'])
        self._is_present(text_confirmation_element,'No se encuentra el mensaje de confirmacion')
        self._is_visible(text_confirmation_element,'El mensaje de confirmacion no encontrado no se encuentra visible')
        actual_text = self._get_text(text_confirmation_element)
        assert text_expected == actual_text , f'El mensaje de confirmacion, no coincide. Se esperaba "{text_expected}" y se obtuvo "{actual_text}"'
