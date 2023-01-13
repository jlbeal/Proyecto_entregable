import factories_drivers.factory_driver as f_driver
from pages.menu_page import MenuPage
from pages.base_page import BasePage

from pages.search_page import SearchPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.product_page import ProductPage

from pages.myaccount_page import MyAccountPage 
from selenium.webdriver.common.by import By
import time


driver = f_driver.get_driver()

first_name = 'Jose Luis'
last_name = 'test1'
email = 'joseluis.ba@gmail.com'
telephone = '1239393333'
password = 'test12'

def test_01_home():
    menu_page = MenuPage(driver)
    menu_page.verificar_carrusel()
    time.sleep(2)

def test_02_register():

    menu_page = MenuPage(driver)
    menu_page.click_my_account()
    menu_page.click_register()
    register_page = RegisterPage(driver)
    register_page.verificar_titulo_register_customer()
    register_page.ingresar_first_name(first_name)
    register_page.ingresar_last_name(last_name)
    register_page.ingresar_email(email)
    register_page.ingresar_telephone(telephone)
    register_page.ingresar_password(password)
    register_page.ingresar_confirm_password(password)
    register_page.click_privacy_policy()
    register_page.click_continue()
    time.sleep(2)

def test03_login():
    menu_page = MenuPage(driver)
    menu_page.click_my_account()
    menu_page.click_logout()
    menu_page.click_my_account()
    menu_page.click_login()
    login_page = LoginPage(driver)
    login_page.ingresar_email(email)
    login_page.ingresar_password(password)
    time.sleep(2)

def test_buscar_product():
    price_iphone = '$123.20'
    titulo_iphone= 'iPhone'

    menu_page = MenuPage(driver)
    menu_page.buscar_producto(titulo_iphone)
    search_page = SearchPage(driver)
    search_page.selecccionar_primer_producto()
    product_page = ProductPage(driver)
    product_page.verificar_titulo_product(titulo_iphone)
    product_page.verificar_imagenes_product()
    product_page.verificar_precio_label(price_iphone)
    product_page.boton_add_to_cart()
    product_page.verificar_mensaje_success()
    time.sleep(2)



def test_search_tabs_monitors():

    price_monitors = '$242.00'
    titulo_monitor = 'Samsung SyncMaster 941BW'

    menu_page = MenuPage(driver)
    menu_page.click_logo()
    menu_page.click_menu_components()
    search_page =SearchPage(driver)
    search_page.selecccionar_segundo_producto_monitors()
    product_page = ProductPage(driver)
    product_page.verificar_titulo_product(titulo_monitor)
    product_page.verificar_precio_label(price_monitors)
    time.sleep(3)

def test_search_tabs_cameras():

    price_camera = '$98.00'
    titulo_camera = 'Canon EOS 5D'

    menu_page = MenuPage(driver)
    menu_page.click_logo()
    menu_page.click_menu_cameras()
    search_page =SearchPage(driver)
    search_page.selecccionar_primer_producto()
    product_page = ProductPage(driver)
    product_page.verificar_titulo_product(titulo_camera)
    product_page.verificar_precio_label(price_camera)
    time.sleep(3)

def test_search_tabs_phones():

    price_phone_htc = '$122.00'
    titulo_phone_htc = 'HTC Touch HD'

    menu_page = MenuPage(driver)
    menu_page.click_logo()
    menu_page.click_menu_phones()
    search_page =SearchPage(driver)
    search_page.selecccionar_primer_producto()
    product_page = ProductPage(driver)
    product_page.verificar_titulo_product(titulo_phone_htc)
    product_page.verificar_precio_label(price_phone_htc)
    time.sleep(3)

def test_login_negativo():

    confirmation_login_text = 'Warning: No match for E-Mail Address and/or Password.'

    menu_page = MenuPage(driver)
    menu_page.click_my_account()
    menu_page.click_login()
    login_page = LoginPage(driver)
    login_page.ingresar_email(email)
    login_page.ingresar_password('password')
    time.sleep(2)
    login_page.click_login()
    time.sleep(2)
    login_page.verificar_confirmacion_login(confirmation_login_text)

def test_register_email_duplicado():

    confirmation_text = 'Warning: E-Mail Address is already registered!'
    
    menu_page = MenuPage(driver)
    menu_page.click_my_account()
    menu_page.click_register()
    register_page = RegisterPage(driver)
    register_page.verificar_titulo_register_customer()
    register_page.ingresar_first_name(first_name)
    register_page.ingresar_last_name(last_name)
    register_page.ingresar_email(email)
    register_page.ingresar_telephone(telephone)
    register_page.ingresar_password(password)
    register_page.ingresar_confirm_password(password)
    register_page.click_privacy_policy()
    register_page.click_continue()
    time.sleep(2)
    register_page.verificar_confirmacion(confirmation_text)
    time.sleep(2)

def testCase1_busqueda():
    producto = 'Display'
    busqueda_invalida_text = 'There is no product that matches the search criteria.'
    menu_page = MenuPage(driver) 
    menu_page.buscar_producto(producto)
    search_page = SearchPage(driver)
    search_page.verificar_no_producto(busqueda_invalida_text)
    search_page.check_product_description()
    search_page.click_search()
    #menu_page.back_landingpage()
    home_page=driver.find_element(By.XPATH,'/html/body/div[2]/ul/li[1]/a/i')
    home_page.click()
    time.sleep(10)

def teardown():
    BasePage(driver).close_browser()