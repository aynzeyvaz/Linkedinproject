import streamlit as st
import pandas as pd
from job_scraper import linkedin

st.set_page_config(page_title="Linkedin jobs")
st.title("LinkedIn 🐼:")


jobtitle=st.text_input("Job Title", placeholder="e.g. , Data Analyst", key="job_title")
location_type=st.selectbox("Location", ["Remote", "Other"], key="location_type")
if location_type=="Other":
    location=st.text_input("Specify the location", placeholder="e.g. Berlin", key="Location")
else:
    location="Remote"

number=st.number_input("Number of results you'd like to see", step=1, min_value=1, key="number")
sub_button=st.button("Search")

if sub_button:
     if jobtitle:
        if location_type == "Other" and not location:
            st.warning("Please enter a location.")
        else:
            with st.spinner("Searching LinkedIn jobs, please wait...⌛"):
                    scraper= linkedin(jobtitle, location, number)
                    scraper.create_driver()
                    scraper.search_URL()
                    scraper.scroller()
                    scraper.jobscraper()
                    scraper.tocsv()
                    scraper.quit()

                    table=pd.read_csv("results.csv")
                    st.success(f"Found {len(table)} jobs!")
                    for index, row in table.iterrows():   #هر سطر در جدولو به صورت دو تایی ایندکس و اون سطر میده
                        with st.container(border=True):
                                if pd.notna(row["Picture"]):
                                    st.image(row["Picture"], width=100)
                                else:
                                     st.write("Unabla to load image.")
                                st.markdown(f"### 📌{row['Title']}")
                                st.markdown(row['Company'])
                                st.markdown(row['Location'])
                                st.markdown(row['Date'])
                                st.markdown(f"<a href='{row['Link']}'>🔗Tap to see the full information! </a>", unsafe_allow_html=True)
                        
     else:
         st.warning("Please enter a Job title.")



