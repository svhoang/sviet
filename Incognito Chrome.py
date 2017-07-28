# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
#how to update PATH library (usr/lib/bin) with new modules
import sys
sys.path.append('C:/Users/elot1z6/AppData/Local/Continuum/Anaconda3/Lib')

#%%s
#open browser to incognito 
from os import system
system("\"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\" -incognito www.gmail.com")
system("\"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\" -incognito www.soundcloud.com")

#%%
#https://sites.google.com/a/chromium.org/chromedriver/getting-started
#https://github.com/seleniumhq/selenium/issues/1689
#https://stackoverflow.com/questions/31349788/using-selenium-in-python-to-click-through-all-elements-with-the-same-class-name

#select for soundcloud signin button -->https://www.youtube.com/watch?v=mW138ljocCM
##content > div > div > div.l-front-hero.l-inner-fullwidth > div > div > div.frontHero__signin > button.g-opacity-transition.frontHero__loginButton.g-button-transparent-inverted.sc-button.sc-button-medium.loginButton

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

executable_path = "C:/Users/elot1z6/Documents/Python Scripts/Selenium/chromedriver/chromedriver.exe"
chrome_options = Options()

#private browsing
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=800,600")
driver = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options)
driver.set_window_position(2000,1000)
website = driver.get('http://www.google.ca')
assert "Google" in driver.title
elem = driver.find_element_by_name('q')
elem.clear()
elem.send_keys("Soundcloud")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source


time.sleep(5) # Let the user actually see something!


#driver.quit()
#%%
#Using Selenium to write test cases
import unittest 

def fun(x):
    return x+1

class MyTest(unittest.TestCase):
    def test(self):
        self.asertEqual(fun(3),4)
        
fun(12)


#%%
#pip
import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)

#%%
#login to gmail

import requests
import BeautifulSoup

class SessionGoogle:
    def __init__(self, url_login, url_auth, login, pwd):
        self.ses = requests.session()
        login_html = self.ses.get(url_login)
        soup_login = BeautifulSoup(login_html.content).find('form').find_all('input')
        my_dict = {}
        for u in soup_login:
            if u.has_attr('value'):
                my_dict[u['name']] = u['value']
        # override the inputs without login and pwd:
        my_dict['Email'] = login
        my_dict['Passwd'] = pwd
        self.ses.post(url_auth, data=my_dict)

    def get(self, URL):
        return self.ses.get(URL).text
    
#function call
url_login = "https://accounts.google.com/ServiceLogin"
url_auth = "https://accounts.google.com/ServiceLoginAuth"
session = SessionGoogle(url_login, url_auth, "myGoogleLogin", "myPassword")
print (session.get("plus.google.com"))


#%% password encryption
#https://stackoverflow.com/questions/157938/hiding-a-password-in-a-python-script-insecure-obfuscation-only
import base64
print (base64.b64encode(b'password'))

print (base64.b64decode("cGFzc3dvcmQ="))
