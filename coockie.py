from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time
import pickle

class Linkdin:
    def __init__(self,geckodriverpath):
        self.service=Service(geckodriverpath)
        self.driver=webdriver.Firefox(service=self.service)
    def openpage(self):
        self.driver.get("https://www.linkedin.com/login")
        time.sleep(10)

test=Linkdin("C:\\Users\\Vivo\\Desktop\\firedriver\\geckodriver.exe")
test.openpage()
with open("C:\\Users\\Vivo\\Desktop\\FinalProject\\coockies.pkl", "wb") as file:
    pickle.dump(test.driver.get_cookies(), file)

print("coockies saved")
