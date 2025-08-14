from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
import os
 

class linkedin():
    def __init__(self, jobtitle, location, number):
        self.jobtitle=jobtitle
        self.location=location
        self.number=number
        self.li=[]
    
    def create_driver(self):
        options=Options()
        options.add_argument("--headless")
        self.driver=webdriver.Firefox(options=options)

    def search_URL(self):
        self.job=self.jobtitle.replace(" ", "%20").lower()
        self.loc=self.location.replace(" ", "%20").replace(",", "%2c").lower()
        self.link=f"https://www.linkedin.com/jobs/search/?keywords={self.job}&location={self.loc}"
        self.driver.get(self.link)
        time.sleep(5)
        try:
            popup=self.driver.find_element(By.XPATH,r"/html/body/div[5]/div/div/section/button") 
            popup.click()
        except NoSuchElementException:
            pass
        


    def scroller(self):
        height=self.driver.execute_script("return document.body.scrollHeight;")
        time.sleep(3)
        for i in range (5):    
            main=self.driver.find_element(By.ID, "main-content")                                           
            self.li.extend(main.find_elements(By.TAG_NAME,"li"))
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            newheight=self.driver.execute_script("return document.body.scrollHeight;")
            if newheight==height:
                break
            height=newheight

    def jobscraper(self):        
        self.titles=[]
        self.companies=[]
        self.locations=[]
        self.dates=[]
        self.links=[]
        self.pictures=[]
        
        for j in self.li:            
            if len (self.titles)>=self.number:
                break
            try:
                title=j.find_element(By.CLASS_NAME, "base-search-card__title").text
                company=j.find_element(By.CLASS_NAME, "base-search-card__subtitle").text
                location=j.find_element(By.CLASS_NAME, "job-search-card__location").text
                date=j.find_element(By.TAG_NAME, "time").text
                linktojob=j.find_element(By.TAG_NAME, "a").get_attribute("href")
                
                picture=j.find_element(By.TAG_NAME, "img").get_attribute("src")
            except:
                continue
            
            if linktojob and linktojob not in self.links:
                if title and company and location and picture and date:
                    self.titles.append(title)
                    self.companies.append(company)
                    self.locations.append(location)
                    self.dates.append(date)
                    self.links.append(linktojob)
                    self.pictures.append(picture)
               # else:
                    #print("Not all elements were available")


    def tocsv(self):
        table=pd.DataFrame({"Title":self.titles,"Company":self.companies, "Location":self.locations,"Date":self.dates, "Link":self.links,"Picture":self.pictures})
        current_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(current_dir,"results.csv")
        table.to_csv(filepath, index=False)

    def quit(self):
        self.driver.quit()

    



 