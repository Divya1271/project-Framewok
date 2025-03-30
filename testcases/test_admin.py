import time

import pytest
from selenium import webdriver

from pageobjects.AdminPage import Admin
from utilities.readProperties import ReadConfig

class Test_004_Admin:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    ur="ESS"
    es="Enabled"
    en="Ram"
    un="Ram123"
    pw="r123"
    cpw="r123"


    def test_adminuser(self,setup):
        self.driver=setup
        self.driver.get(self.base_url)
        self.am=Admin(self.driver)
        self.am.enterUserName(self.username)
        self.am.setPassword(self.password)
        self.am.clickLogin()
        time.sleep(5)
        assert "dashboard" in self.driver.current_url, "Login failed or URL not redirected to dashboard."
        self.am.clickAdminButton()
        self.am.clickAddButton()
        self.am.addUserRole(self.ur)
        self.am.addStatus(self.es)
        self.am.addEmployeeName(self.en)
        self.am.addUsername(self.un)
        self.am.addPassword(self.pw)
        self.am.addConfirmPassword(self.cpw)
        self.am.clickSaveButton()
