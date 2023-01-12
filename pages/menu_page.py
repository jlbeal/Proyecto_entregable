from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MenuPage(BasePage):

    __button_search = {'by':By.CSS_SELECTOR, 'locator':'#search button'}
    __input_buscar = {'by':By.NAME,'locator':'search'}
    __img_logo = {'by':By.CSS_SELECTOR,'locator':'#logo img'}
    __carrusel_img = {'by':By.ID,'locator':'slideshow0'}
    __my_account_dropdown = {'by':By.XPATH,'locator':'//ul[@class="list-inline"]//a[@title="My Account"]'}
    __login_option = {'by':By.XPATH,'locator':'//ul[@class="dropdown-menu dropdown-menu-right"]//a[text()="Login"]'}
    __logout_option = {'by':By.XPATH,'locator':'//ul[@class="dropdown-menu dropdown-menu-right"]//a[text()="Logout"]'}
    __register_option = {'by':By.XPATH,'locator':'//ul[@class="dropdown-menu dropdown-menu-right"]//a[text()="Register"]'}
    __checkout_option = {'by':By.XPATH,'locator':'//a[@title="Checkout"]'}
    __shopping_option = {'by':By.XPATH,'locator':'//a[@title="Shopping Cart"]'}
    __components_menu = {'by':By.XPATH,'locator':'//li[@class="dropdown"]//a[text()="Components"]'}
    __option_monitor = {'by':By.XPATH,'locator':'//ul[@class="list-unstyled"]//a[text()="Monitors (2)"]'}
    __cameras_menu = {'by':By.XPATH,'locator':'//ul//li//a[text()="Cameras"]'}
    __phones_menu = {'by':By.XPATH,'locator':'//ul//li//a[text()="Phones & PDAs"]'}

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.__verificar_logo()
        
    def __verificar_logo(self):
        img_element = self._get_element(self.__img_logo['by'],self.__img_logo['locator'])
        self._is_present(img_element,'No se encuentra la Imagen del Logo')
        self._is_visible(img_element,'El Logo no se encuentra visible')

    def click_logo(self):
        logo_button = self._get_element(self.__img_logo['by'], self.__img_logo['locator'])
        self._is_present(logo_button, 'No se encuentra el logo')
        self._is_visible(logo_button, 'El logo no se encuentra visible') 
        self._is_enabled(logo_button, 'El logo no se encuentra habilitado') 
        self._click(logo_button)

    def verificar_carrusel(self):
        carrusel_element = self._get_element(self.__carrusel_img['by'],self.__carrusel_img['locator'])
        self._is_present(carrusel_element, 'No se encuentra el carrusel')
        self._is_visible(carrusel_element, 'El carrusel no se encuentra visible') 
        self._is_enabled(carrusel_element, 'El carrusel no se encuentra habilitado') 

    def click_boton_buscar(self):
        button_element = self._get_element(self.__button_search['by'], self.__button_search['locator'])
        self._is_present(button_element, 'No se encuentra el boton Buscar')
        self._is_visible(button_element, 'El boton buscar no se encuentra visible') 
        self._is_enabled(button_element, 'El boton de Busqueda no se encuentra habilitado') 
        self._click(button_element)

    def ingresar_busqueda(self,text):
        input_element = self._get_element(self.__input_buscar['by'],self.__input_buscar['locator'])
        self._is_present(input_element,'No se encuentra el input de Busqueda')
        self._is_visible(input_element,'El input de Busqueda no se encuentra visible')
        self._write(input_element,text)

    def borrar_busqueda(self):
        input_element = self._get_element(self.__input_buscar['by'],self.__input_buscar['locator'])
        self._is_present(input_element,'No se encuentra el input de Busqueda')
        self._is_visible(input_element,'El input de Busqueda no se encuentra visible')
        self._clear_field(input_element)

    def buscar_producto(self,text):
        self.ingresar_busqueda(text)
        self.click_boton_buscar()

    def click_my_account(self):
        my_account_element = self._get_element(self.__my_account_dropdown['by'],self.__my_account_dropdown['locator'])
        self._is_present(my_account_element, 'No se encuentra el campo My Account')
        self._is_visible(my_account_element, 'El campo My Account no se encuentra visible') 
        self._is_enabled(my_account_element, 'El campo My Account no se encuentra habilitado') 
        self._click(my_account_element)

    def click_login(self):
        login_element = self._get_element(self.__login_option['by'],self.__login_option['locator'])
        self._is_present(login_element, 'No se encuentra la opcion login')
        self._is_visible(login_element, 'La opcion login no se encuentra visible') 
        self._is_enabled(login_element, 'La opcion login no se encuentra habilitado') 
        self._click(login_element)
    
    def click_logout(self):
        logout_element = self._get_element(self.__logout_option['by'],self.__logout_option['locator'])
        self._is_present(logout_element, 'No se encuentra la opcion logout')
        self._is_visible(logout_element, 'La opcion logout no se encuentra visible') 
        self._is_enabled(logout_element, 'La opcion logout no se encuentra habilitado') 
        self._click(logout_element)

    def click_register(self):
        register_element = self._get_element(self.__register_option['by'],self.__register_option['locator'])
        self._is_present(register_element, 'No se encuentra la opcion register')
        self._is_visible(register_element, 'La opcion register no se encuentra visible') 
        self._is_enabled(register_element, 'La opcion register no se encuentra habilitado') 
        self._click(register_element)

    def click_checkout(self):
        checkout_element = self._get_element(self.__checkout_option['by'],self.__checkout_option['locator'])
        self._is_present(checkout_element, 'No se encuentra la opcion Checkout')
        self._is_visible(checkout_element, 'La opcion Checkout no se encuentra visible') 
        self._is_enabled(checkout_element, 'La opcion Checkout no se encuentra habilitado') 
        self._click(checkout_element)

    def click_shopping_cart(self):
        shopping_element = self._get_element(self.__shopping_option['by'],self.__shopping_option['locator'])
        self._is_present(shopping_element, 'No se encuentra la opcion Shopping cart')
        self._is_visible(shopping_element, 'La opcion Shopping cart no se encuentra visible') 
        self._is_enabled(shopping_element, 'La opcion Shopping cart no se encuentra habilitado') 
        self._click(shopping_element)

    def click_menu_components(self):
        components_option = self._get_element(self.__components_menu['by'],self.__components_menu['locator'])
        self._is_present(components_option, 'No se encuentra la opcion Components')
        self._is_visible(components_option, 'La opcion Components no se encuentra visible') 
        self._is_enabled(components_option, 'La opcion Components no se encuentra habilitado') 
        self._click(components_option)
        monitors_option = self._get_element(self.__option_monitor['by'],self.__option_monitor['locator'])
        self._is_present(monitors_option, 'No se encuentra la opcion Monitors')
        self._is_visible(monitors_option, 'La opcion Monitors no se encuentra visible') 
        self._is_enabled(monitors_option, 'La opcion Monitors no se encuentra habilitado') 
        self._click(monitors_option)

    def click_menu_cameras(self):
        cameras_option = self._get_element(self.__cameras_menu['by'],self.__cameras_menu['locator'])
        self._is_present(cameras_option, 'No se encuentra la opcion Cameras')
        self._is_visible(cameras_option, 'La opcion Cameras no se encuentra visible') 
        self._is_enabled(cameras_option, 'La opcion Cameras no se encuentra habilitado') 
        self._click(cameras_option)

    def click_menu_phones(self):
        phones_option = self._get_element(self.__phones_menu['by'],self.__phones_menu['locator'])
        self._is_present(phones_option, 'No se encuentra la opcion Phones & PDAs')
        self._is_visible(phones_option, 'La opcion Phones & PDAs no se encuentra visible') 
        self._is_enabled(phones_option, 'La opcion Phones & PDAs no se encuentra habilitado') 
        self._click(phones_option)