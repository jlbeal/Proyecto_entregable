from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    
    __product_page = {'by':By.ID, 'locator':'product-product'}
    __product_titulo = {'by':By.XPATH, 'locator':'//div[@id="content"]//h1'}
    __product_images = {'by':By.CLASS_NAME, 'locator':'thumbnails'}
    __price_label = {'by':By.XPATH, 'locator':'//li//h2'}
    __cart_button = {'by':By.ID, 'locator':'button-cart'}
    __message_success = {'by':By.XPATH, 'locator':'//div[@class = "alert alert-success alert-dismissible"]'}


    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.__verificar_pagina_product()

    def __verificar_pagina_product(self):
        product_page = self._get_element(self.__product_page['by'],self.__product_page['locator'])
        self._is_present(product_page,'No se encuentra la pagina de Producto')
        self._is_visible(product_page,'La pagina de Producto no se encuentra visible')

    def verificar_titulo_product(self,text_expected):
        titulo_product = self._get_element(self.__product_titulo['by'],self.__product_titulo['locator'])
        self._is_present(titulo_product,'No se encuentra el titulo del producto')
        self._is_visible(titulo_product,'El titulo del producto no se encuentra visible')
        actual_text = self._get_text(titulo_product)
        assert text_expected == actual_text , f'El mensaje de confirmacion, no coincide. Se esperaba "{text_expected}" y se obtuvo "{actual_text}"'

    def verificar_imagenes_product(self):
        imagenes_product = self._get_element(self.__product_images['by'],self.__product_images['locator'])
        self._is_present(imagenes_product,'No se encuentra las imagenes del producto')
        self._is_visible(imagenes_product,'Las imagenes del producto no se encuentra visible')

    def verificar_precio_label(self,text_expected):
        precio_label = self._get_element(self.__price_label['by'],self.__price_label['locator'])
        self._is_present(precio_label,'No se encuentra el label del precio')
        self._is_visible(precio_label,'El label del precio no se encuentra visible')
        actual_text = self._get_text(precio_label)
        assert text_expected == actual_text , f'El mensaje de confirmacion, no coincide. Se esperaba "{text_expected}" y se obtuvo "{actual_text}"'

    def boton_add_to_cart(self):
        button_cart_element = self._get_element(self.__cart_button['by'],self.__cart_button['locator'])
        self._is_present(button_cart_element, 'No se encuentra el boton Add to Cart')
        self._is_visible(button_cart_element, 'El boton Add to Cart no se encuentra visible') 
        self._is_enabled(button_cart_element, 'El boton Add to Cart no se encuentra habilitado') 
        self._click(button_cart_element)

    def verificar_mensaje_success(self):
        mensaje_success = self._get_element(self.__message_success['by'],self.__message_success['locator'])
        self._is_present(mensaje_success,'No se encuentra el mensaje de success')
        self._is_visible(mensaje_success,'El mensaje de success no se encuentra visible')
       
    