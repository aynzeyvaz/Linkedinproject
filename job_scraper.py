from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd
import os
 

class linkedin():
    def __init__(self, jobtitle, location, number):
        self.jobtitle=jobtitle
        self.location=location
        self.number=number
    
    def create_driver(self):
        options=Options()
        options.add_argument("--headless")
        self.driver=webdriver.Firefox(options=options)

    def search_URL(self):
        self.job=self.jobtitle.replace(" ", "%20").lower()
        self.loc=self.location.replace(" ", "%20").replace(",", "%2c").lower()
        self.link=f"https://www.linkedin.com/jobs/search/?keywords={self.job}&location={self.loc}"
        self.driver.get(self.link)
        time.sleep(3)

    def job_scraper(self):
        
        height=self.driver.execute_script("return document.body.scrollHeight;")
        self.jobs=[]

        for i in range (5):                                               
            self.jobs.extend(self.driver.find_elements(By.CLASS_NAME, "base-card"))
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            newheight=self.driver.execute_script("return document.body.scrollHeight;")
            if newheight==height:
                break
            height=newheight
        
        titles=[]
        companies=[]
        locations=[]
        links=[]
        pictures=[]

        for j in self.jobs:
            if len (titles)>=self.number:
                print(len(titles))
                break
            title=j.find_element(By.CLASS_NAME, "base-search-card__title").text.strip()
            company=j.find_element(By.CLASS_NAME, "base-search-card__subtitle").text.strip()
            location=j.find_element(By.CLASS_NAME, "job-search-card__location").text.strip()
            linktojob=j.find_element(By.TAG_NAME, "a").get_attribute("href").strip()
            picture=j.find_element(By.TAG_NAME, "img").get_attribute("src")
            if title and company and location and linktojob:
                titles.append(title)
                companies.append(company)
                locations.append(location)
                links.append(linktojob)
                pictures.append(picture)
            
        table=pd.DataFrame({ "Title": titles, "Company":companies, "Location": locations, "Link": links, "Picture": pictures})
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(current_dir,"results.csv")
        table.to_csv(filepath, index=False)
        self.driver.quit()



 