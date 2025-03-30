import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    def __init__(self,driver):
        self.driver=driver
        time.sleep(5)
        self.username_box=(By.NAME, "username")
        self.password_box=(By.NAME, "password")
        self.login_button=(By.XPATH, "//button[@type='submit']")


    def enterUserName(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_box)
        ).send_keys(username)

    def setPassword(self,password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_box)
        ).send_keys(password)

    def clickLogin(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_button)
        ).click()



