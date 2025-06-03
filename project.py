from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

class Linkdin:
    def __init__(self,chromedriverpath):
        self.service=Service(chromedriverpath)
        self.driver=webdriver.Chrome(service=self.service)
    def openpage(self):
        self.driver.get("https://www.linkedin.com/jobs/")
        time.sleep(5)
    def closepage(self):
        self.driver.quit()

