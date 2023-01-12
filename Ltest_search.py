import factories_drivers.factory_driver as f_driver
from pages.base_page import BasePage
from pages.menu_page import MenuPage
from pages.search_page import SearchPage
from pages.myaccount_page import MyAccountPage 
import time
from selenium.webdriver.common.by import By

driver = f_driver.get_driver()


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

def testCase2_register():
     firstName = 'Lupita'
     lastName = 'Aguirre'
     email = 'test@test.com'
     telefono = '123456789'
     password = 'password'
     passwordConfirm = 'password'

    #driver.find_element_by_xpath('//*[@id="input-firstname"]').send_keys(firstName)
    #driver.find_element_by_xpath('//*[@id="input-lastname"]').send_keys(lastName)
    #driver.find_element_by_xpath('//*[@id="input-email"]').send_keys(email)
    #driver.find_element_by_xpath('//*[@id="input-telephone"]').send_keys(telefono)
    #driver.find_element_by_xpath('//*[@id="input-password"]').send_keys(password)
    #driver.find_element_by_xpath('//*[@id="input-confirm"]').send_keys(passwordConfirm)
    #/html/body/div[2]/div[2]/div/form/div/div/input[1]
     myaccount_page = MyAccountPage(driver)
     myaccount_page.click_register()
     myaccount_page.register(firstName, lastName, email, telefono, password, passwordConfirm)
     myaccount_page.click_submit_register()
     time.sleep(10)



def testCase3_login():
    usuario = 'test@test.com'
    password = 'password'
    myaccount_page = MyAccountPage(driver)
    #myaccount_page.click_myaccount()
    #myaccount_page.click_login()
    myacc_page=driver.find_element(By.XPATH,'/html/body/footer/div/div/div[4]/ul/li[1]/a')
    myacc_page.click()
    myaccount_page.login(usuario, password)
    time.sleep(10)

def testCase3_busqueda():
 #producto = 'Display'
 #busqueda_invalida_text = 'There is no product that matches the search criteria.'
 #menu_page = MenuPage(driver) 
 #menu_page.buscar_producto(producto)
 #search_page = SearchPage(driver)
 #search_page.verificar_no_producto(busqueda_invalida_text)
 #search_page.check_product_description()
 #search_page.click_search()
 #time.sleep(2)


#def testCase4_product():
#def testCase5_checkout():
#def teardown():




#BasePage(driver).close_browser()


