import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from data import data_login
from page import locator

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())

    def test_Login_Empty_Password(self):
        driver=self.driver
        driver.get("https://www.saucedemo.com/") 
        driver.maximize_window()
        driver.find_element(By.ID,locator.username).send_keys(data_login.valid_username)
        time.sleep(1)
        driver.find_element(By.ID,locator.password).send_keys(data_login.empty_password)
        time.sleep(1)
        driver.find_element(By.ID,locator.login_button).click()
        time.sleep(5)

        response_message=driver.find_element(By.CSS_SELECTOR,locator.alert).text
        self.assertEqual(response_message,'Epic sadface: Password is required')

    def test_Login_Invalid_Password(self):
        driver=self.driver
        driver.get("https://www.saucedemo.com/") 
        driver.maximize_window()
        driver.find_element(By.ID,locator.username).send_keys(data_login.valid_username)
        time.sleep(1)
        driver.find_element(By.ID,locator.password).send_keys(data_login.invalid_password)
        time.sleep(1)
        driver.find_element(By.ID,locator.login_button).click()
        time.sleep(2)

        response_message=driver.find_element(By.CSS_SELECTOR,locator.alert).text
        self.assertEqual(response_message,'Epic sadface: Username and password do not match any user in this service')

    def test_Login_Invalid_Username(self):
        driver=self.driver
        driver.get("https://www.saucedemo.com/") 
        driver.maximize_window()
        driver.find_element(By.ID,locator.username).send_keys(data_login.invalid_username)
        time.sleep(1)
        driver.find_element(By.ID,locator.password).send_keys(data_login.valid_password)
        time.sleep(1)
        driver.find_element(By.ID,locator.login_button).click()
        time.sleep(2)

        response_message=driver.find_element(By.CSS_SELECTOR,locator.alert).text
        self.assertEqual(response_message,'Epic sadface: Username and password do not match any user in this service') 

    def test_Login_Empty_Username(self):
        driver=self.driver
        driver.get("https://www.saucedemo.com/") 
        driver.maximize_window()
        driver.find_element(By.ID,locator.username).send_keys(data_login.empty_username)
        time.sleep(1)
        driver.find_element(By.ID,locator.password).send_keys(data_login.valid_password)
        time.sleep(1)
        driver.find_element(By.ID,locator.login_button).click()
        time.sleep(2)

        response_message=driver.find_element(By.CSS_SELECTOR,locator.alert).text
        self.assertEqual(response_message,'Epic sadface: Username is required') 

    def test_Login_Success_Login(self):
        driver=self.driver
        driver.get("https://www.saucedemo.com/") 
        driver.maximize_window()
        driver.find_element(By.ID,locator.username).send_keys(data_login.valid_username)
        time.sleep(1)
        driver.find_element(By.ID,locator.password).send_keys(data_login.valid_password)
        time.sleep(1)
        driver.find_element(By.ID,locator.login_button).click()
        time.sleep(2)

        driver.get("https://www.saucedemo.com/inventory.html");   

    def tearDown(self):
        self.driver.close()    

unittest.main()        
