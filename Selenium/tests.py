from pom import LoginPage
from time import sleep
from selenium import webdriver


driver = webdriver.Chrome()
page = LoginPage(driver)
page.open()
page.enter_username('Patryk')
page.enter_password()
page.print_page_info()
page.click_login()
sleep(3)