from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username='taylorlenastyles@gmail.com'
password='13851385a'
class Linkdin:
    def __init__(self,geckodriverpath):
        self.service=Service(geckodriverpath)
        self.driver=webdriver.Firefox(service=self.service)

    def openpage(self):
        self.driver.get("https://www.linkedin.com/login")
        time.sleep(5)

    def closepage(self):
        self.driver.quit()


    def search(self):
        wait=WebDriverWait(self.driver, 10)
        jobs= wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/jobs/']")))
        jobs.click()
        time.sleep(3)

    def login(self,username,password):
        username_input=self.driver.find_element(By.ID, "username")
        username_input.send_keys(username)
        password_input=self.driver.find_element(By.ID, "password")
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(60)

jobfind=Linkdin("C:\\Users\\Vivo\\Desktop\\firedriver\\geckodriver.exe")
jobfind.openpage()
jobfind.login(username,password)
jobfind.search()

