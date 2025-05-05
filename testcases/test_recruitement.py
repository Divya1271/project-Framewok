import time

import pytest
from selenium import webdriver
from pageobjects.Recruitment import Recruit
from utilities.readProperties import ReadConfig

class Test_005_Recruitement:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    fname="Anjali"
    lname="Aghi"
    eid="anjaliaghi56@example.com"
    vcy="Payroll Administrator"

    def test_recruitement(self,setup):
        self.driver=setup
        self.driver.get(self.base_url)
        self.r=Recruit(self.driver)
        self.r.enterUserName(self.username)
        self.r.setPassword(self.password)
        self.r.clickLogin()
        time.sleep(5)
        assert "dashboard" in self.driver.current_url, "Login failed or URL not redirected to dashboard."
        self.r.clickrecruitment()
        self.r.clickaddbutton()
        self.r.clickfirstname(self.fname)
        self.r.clicklastname(self.lname)
        self.r.clickemailid(self.eid)
        self.r.clickjobvacancydd()
        self.r.clickvacancy(self.vcy)
        self.r.clicksavebutton()
        time.sleep(5)
        print("Successfully added")