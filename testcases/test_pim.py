import time

import pytest
from selenium import webdriver
from pageobjects.PimPage import Pim
from utilities.readProperties import ReadConfig

class Test_003_Pim:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    fn="Manoj"
    mn="Kumar"
    ln="Sharma"
    id="1234"


    def test_pimuser(self,setup):
        self.driver=setup
        self.driver.get(self.base_url)
        self.pm=Pim(self.driver)
        self.pm.enterUserName(self.username)
        self.pm.setPassword(self.password)
        self.pm.clickLogin()
        time.sleep(5)
        assert "dashboard" in self.driver.current_url, "Login failed or URL not redirected to dashboard."
        self.pm.clickpimbutton()
        self.pm.clickaddbutton()
        self.pm.addfirstname(self.fn)
        self.pm.addmiddlename(self.mn)
        self.pm.addlastname(self.ln)
        self.pm.addemployeeid(self.id)
        self.pm.clicksavebutton()
        # self.pm.getSuccessMessage()
        time.sleep(5)
        # assert "Successfully Saved" in self.pm.getSuccessMessage(), "User not added successfully."

