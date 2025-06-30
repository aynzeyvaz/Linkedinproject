from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

username="taylorlenastyles@gmail.com"
password="13851385a"

class linkedin:
    def __init__(self):
        self.driver=webdriver.Firefox()
        
    def login(self):
        self.driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
        username_input=self.driver.find_element(By.ID, "username")
        password_input=self.driver.find_element(By.ID, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

hello=linkedin()
hello.login()
