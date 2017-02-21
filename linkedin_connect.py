# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint
from time import sleep
import sys
from urllib import urlencode
import traceback
import json
import argparse
import os
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

reload(sys)
sys.setdefaultencoding('utf8')

class LinkedinConnect():
    def __init__(self):
        self.base_url = "https://www.linkedin.com"

    def init_driver(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.username = raw_input('linkedin username:')
        self.password = raw_input('linkedin password:')

    # This function will open the browser, login to linkedin, then save all search results for the company
    # specified in the company variable
    def linkedin_connect(self):
        self.init_driver()
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("login-email").clear()
        driver.find_element_by_id("login-email").send_keys(self.username)
        driver.find_element_by_id("login-password").clear()
        driver.find_element_by_id("login-password").send_keys(self.password)
        driver.find_element_by_id("login-submit").click()

        # wait until the class appears
        while not driver.find_elements_by_xpath('//div[contains(@class, \"feed-s-identity-module__premium-overlay\")]'):
                sleep(50.0/1000.0)

        while True:
	        driver.get(self.base_url + "/mynetwork/")

	        # Sans-15px-black-85%-semibold inline-block mt1 mb4 ember-view
	        # wait until the class appears

	        while not driver.find_elements_by_xpath('//div[contains(@class, \"mn-connections-summary\")]'):
	                sleep(50.0/1000.0)
	                print "Sleeping"

	        # mn-person-card__person-btn-ext button-secondary-medium
	        #while True:
	        driver.execute_script("var o = document.getElementsByClassName(\"mn-person-card__person-btn-ext button-secondary-medium\"); for (var i = 0; i < o.length; i++){    o[i].click();    console.log(i);}");



def main():
    parser = argparse.ArgumentParser(description='Scrape Linkedin profiles for a specified company')
    args = parser.parse_args()

    
    lip = LinkedinConnect()
    lip.linkedin_connect()


if __name__ == "__main__":
    main()
    # test()