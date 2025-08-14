import streamlit as st
import pandas as pd
from job_scraper import linkedin
from PIL import Image



class Gui:
    def __init__(self):
        st.set_page_config(page_title="Linkedin jobs")
        col1, col2=st.columns([5,1])
        with col1:
            st.title("Search for jobs in LinkedIn🐋")
        with col2:
            man=Image.open("linkedinlogo.png")
            st.image(man, use_container_width=True)

             
             

    def form(self):
            self.jobtitle=st.text_input("Job Title", placeholder="e.g. , Data Analyst", key="job_title")
            self.location_type=st.selectbox("Location", ["Remote", "Other"], key="location_type")
            if self.location_type=="Other":
                self.location=st.text_input("Specify the location", placeholder="e.g. Berlin", key="Location")
            else:
                self.location="Remote"

            self.number=st.number_input("Number of results you'd like to see", step=1, min_value=1, key="number")
            self.sub_button=st.button("Search")

      

    def searcher(self):
        if self.sub_button:
            if self.jobtitle:
                if self.location_type == "Other" and not self.location:
                    st.warning("Please enter a location.")
                else:
                    with st.spinner("Searching LinkedIn jobs, please wait...⌛"):
                            scraper= linkedin(self.jobtitle, self.location, self.number)
                            scraper.create_driver()
                            scraper.search_URL()
                            scraper.scroller()
                            scraper.jobscraper()
                            scraper.tocsv()
                            scraper.quit()

            else:
                st.warning("Please enter a Job title.")
                
    def show(self):
        table=pd.read_csv("results.csv")
        for index, row in table.iterrows():   #هر سطر در جدولو به صورت دو تایی ایندکس و اون سطر میده
            with st.container(border=True):
                    col1, col2=st.columns([1,2])
                    with col1:
                        if pd.notna(row["Picture"]):
                            st.image(row["Picture"], width=150)
                            st.markdown(f"<a href='{row['Link']}'> View Job Info! </a>", unsafe_allow_html=True)
                            
                        else:
                                st.write("Unabla to load image.")
                                st.markdown(f"<a href='{row['Link']}'> View Job Info! </a>", unsafe_allow_html=True)
                            
                    
                    with col2:
                        st.markdown(f"<h3> 📌 {row['Title']}</h3>", unsafe_allow_html=True)
                        st.write(f"{row['Company']}")
                        st.write(f"{row['Location']}")
                        st.caption(f"{row['Date']}")
                        
                        
                        
 
         



