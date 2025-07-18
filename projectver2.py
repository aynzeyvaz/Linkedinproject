from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd


jobtitle=input("What job title do u want to search for? ")
location=input("Which location? ")
number=int(input("How many results would u like to see? "))    #the number does not work correctly

job=jobtitle.replace(" ", "%20").lower()
loc=location.replace(" ", "%20").replace(",", "%2c").lower()

options=Options()
options.add_argument("--headless")
driver=webdriver.Firefox(options=options)
link=f"https://www.linkedin.com/jobs/search/?keywords={job}&location={loc}"
driver.get(link)
time.sleep(3)
height=driver.execute_script("return document.body.scrollHeight;")      #JS code that returns the height of the page
max=10
n=0
while True:                                               #i think there might be a better way to scroll down, more efficeint one!
      if n==max:
           break
      jobs=driver.find_elements(By.CLASS_NAME, "base-card")
      if len(jobs)>=number:
           break
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(3)
      n+=1
      


count=0
list=[]
titles=[]
companies=[]
locations=[]
links=[]
for j in jobs[:number]:
    title=j.find_element(By.CLASS_NAME, "base-search-card__title").text.strip()
    company=j.find_element(By.CLASS_NAME, "base-search-card__subtitle").text.strip()
    location=j.find_element(By.CLASS_NAME, "job-search-card__location").text.strip()
    linktojob=j.find_element(By.TAG_NAME, "a").get_attribute("href").strip()
    if title and company and location and linktojob:
         titles.append(title)
         companies.append(company)
         locations.append(location)
         links.append(linktojob)
  
table=pd.DataFrame({ "Title": titles, "Company":companies, "Location": locations, "Link": links})
print(table.to_string())
table.drop_duplicates(inplace=True)
table.to_csv("C:\\Users\\Vivo\\Desktop\\Folders\\FinalProject\\results.csv")
 