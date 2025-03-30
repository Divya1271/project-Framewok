import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Admin:
    def __init__(self, driver):
        self.driver = driver
        self.username_box=(By.NAME, "username")
        self.password_box=(By.NAME, "password")
        self.login_button=(By.XPATH, "//button[@type='submit']")
        self.admin_button= (By.XPATH, "//a[contains(@href, 'admin')]")
        self.add_button= (By.XPATH, "//button[normalize-space()='Add']")
        self.user_role_dropdown = (By.XPATH, "//label[contains(text(), 'User Role')]/following-sibling::div//div[@class='oxd-select-text']")
        self.status_dropdown = (By.XPATH, "//label[contains(text(), 'Status')]/following-sibling::div//div[@class='oxd-select-text']")
        self.employee_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.username = (By.XPATH, "//label[contains(text(), 'Username')]/following-sibling::div/input")
        self.password = (By.XPATH, "//label[contains(text(), 'Password')]/following-sibling::div/input")
        self.confirm_password = (By.XPATH, "//label[contains(text(), 'Confirm Password')]/following-sibling::div/input")
        self.save_button = (By.XPATH, "//button[contains(text(), 'Save')]")

    def enterUserName(self,username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_box)
        ).send_keys(username)

    def setPassword(self, password):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.password_box)
            ).send_keys(password)

    def clickLogin(self):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.login_button)
            ).click()



