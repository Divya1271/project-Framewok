import time

import pytest
from selenium import webdriver
from pageobjects.PimPage import Pim
from pageobjects.SearchPage import Search
from utilities.readProperties import ReadConfig

class Test_004_Search:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    si="PIM"

    def test_search(self,setup):
        self.driver=setup
        self.driver.get(self.base_url)
        self.s=Search(self.driver)
        self.s.enterUserName(self.username)
        self.s.setPassword(self.password)
        self.s.clickLogin()
        time.sleep(5)
        assert "dashboard" in self.driver.current_url, "Login failed or URL not redirected to dashboard."
        self.s.clicksearchbutton()
        self.s.addsearchitem(self.si)
        time.sleep(5)
        print("Search successfull")