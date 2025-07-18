from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd


jobtitle=input("What job title do u want to search for? ")
location=input("Which location? ")
number=int(input("How many results would u like to see? "))             

job=jobtitle.replace(" ", "%20").lower()
loc=location.replace(" ", "%20").replace(",", "%2c").lower()

#options=Options()
#options.add_argument("--headless")
driver=webdriver.Firefox() #options=options
link=f"https://www.linkedin.com/jobs/search/?keywords={job}&location={loc}"
driver.get(link)
time.sleep(3)


height=driver.execute_script("return document.body.scrollHeight;")    
jobs=[]
for i in range(5):                                               
     jobs.extend(driver.find_elements(By.CLASS_NAME, "base-card"))
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     time.sleep(3)
     newheight=driver.execute_script("return document.body.scrollHeight;")
     if newheight==height:
          break
     height=newheight
      
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
 