from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

username="taylorlenastyles@gmail.com"
password="13851385a"

jobtitle=input("What job title do u want to search for?")
number=input("How many results should be shown?")
location=input("Which location?")

class linkedin:
    def __init__(self):
        self.driver=webdriver.Firefox()
        
    def login(self):
        URL="linkedin.com/jobs/search?keywords="+"jobtitle"+"&position=1&pagenum=0"
        self.driver.get(URL)
        username_input=self.driver.find_element(By.ID, "username")
        password_input=self.driver.find_element(By.ID, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

hello=linkedin()
hello.login()
