from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MyAccountPage(BasePage):

    __top_navbar = {'by':By.ID,'locator':'top'} #/html/body/nav/div/div[2]/ul/li[2]/a
    __button_myaccount = {'by':By.XPATH,'locator':'/html/body/nav/div/div[2]/ul/li[2]/a'}
    __button_register = {'by':By.XPATH,'locator':'/html/body/nav/div/div[2]/ul/li[2]/ul/li[1]/a'}
    __button_login = {'by':By.XPATH,'locator':'/html/body/nav/div/div[2]/ul/li[2]/ul/li[2]/a'}
    __button_submit_register = {'by':By.XPATH,'locator':'/html/body/div[2]/div/div/form/div/div/input[2]'}
    __button_submit_login = {'by':By.XPATH,'locator':'/html/body/div[2]/div/div/div/div[2]/div/form/input'}
    __input_login =  {'by':By.ID,'locator':'input-email'} #//*[@id="input-email"]
    __input_login_pwd =  {'by':By.ID,'locator':'input-password'} #//*[@id="input-email"]
    __input_register_fn = {'by':By.ID,'locator':'input-firstname'}
    __input_register_ln = {'by':By.ID,'locator':'input-lastname'}
    __input_register_email = {'by':By.ID,'locator':'input-email'}
    __input_register_telefono = {'by':By.ID,'locator':'input-telephone'}
    __input_register_pwd = {'by':By.ID,'locator':'input-password'}
    __input_register_pwd_c = {'by':By.ID,'locator': 'input-confirm'}



    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.__verificar_myaccount()

    def __verificar_myaccount(self):
        content_element = self._get_element(self.__top_navbar['by'],self.__top_navbar['locator'])
        self._is_present(content_element,'No se encuentra el top de navbar')
        self._is_visible(content_element,'El top de navbar no se encuentra visible')

 
    def click_myaccount(self):
        button_element = self._get_element(self.__button_myaccount['by'],self.__button_myaccount['locator'])
        self._is_present(button_element,'No se encuentra el tab de My account')
        self._is_visible(button_element,'El Boton de MyAccount no se encuentra Visible')
        self._is_enabled(button_element,'El Boton de MyAccount no se encuentra Habilitado')
        self._click(button_element)
        #agregar login
        #button_element2 = self._get_element(self.__button_login['by'],self.__button_login['locator'])
        #self._is_present(button_element2,'No se encuentra el dropdown de Login')
        #self._is_visible(button_element2,'El dropdown de Login no se encuentra Visible')
        #self._is_enabled(button_element2,'El dropdown de Login no se encuentra Habilitado')
        #self._click(button_element2)
    

        
    def click_register(self):
        button_element = self._get_element(self.__button_register['by'],self.__button_register['locator'])
        self._is_present(button_element,'No se encuentra el dropdown de Register')
        self._is_visible(button_element,'El dropdown de Register no se encuentra Visible')
        self._is_enabled(button_element,'El dropdown de Register no se encuentra Habilitado')
        self._click(button_element)
        
    def click_login(self):
        button_element = self._get_element(self.__button_login['by'],self.__button_login['locator'])
        self._is_present(button_element,'No se encuentra el dropdown de Login')
        self._is_visible(button_element,'El dropdown de Login no se encuentra Visible')
        self._is_enabled(button_element,'El dropdown de Login no se encuentra Habilitado')
        self._click(button_element)
    
    def click_submit_register(self):
        button_element = self._get_element(self.__button_submit_register['by'],self.__button_submit_register['locator'])
        self._is_present(button_element,'No se encuentra el boton de submit')
        self._is_visible(button_element,'No se encuentra Visible')
        self._is_enabled(button_element,'No se encuentra Habilitado')
        self._click(button_element)

    def click_submit_login(self):
        button_element = self._get_element(self.__button_submit_login['by'],self.__button_submit_login['locator'])
        self._is_present(button_element,'No se encuentra el boton de submit')
        self._is_visible(button_element,'No se encuentra Visible')
        self._is_enabled(button_element,'No se encuentra Habilitado')
        self._click(button_element)

    #def register(self,text):
        #input_element = self._get_element(self.__input_register['by'],self.__input_register['locator'])
        #self._is_present(input_element,'No se encuentra el input de Busqueda')
        #self._is_visible(input_element,'El input de Busqueda no se encuentra visible')
        #self._write(input_element,text)

    def login(self,text1, text2):
        input_element_user1 = self._get_element(self.__input_login['by'],self.__input_login['locator'])
        input_element_user2 = self._get_element(self.__input_login_pwd['by'],self.__input_login_pwd['locator'])

        
        self._is_present(input_element_user1,'No se encuentra el input de Busqueda')
        self._is_visible(input_element_user1,'El input de Busqueda no se encuentra visible')
        self._write(input_element_user1,text1)
        self._write(input_element_user2, text2)
        button_element = self._get_element(self.__button_submit_login['by'],self.__button_submit_login['locator'])
        self._click(button_element)