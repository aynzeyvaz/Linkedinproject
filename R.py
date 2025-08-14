from job_scraper import linkedin
from streamlit_part import Gui
import streamlit as st
import pandas as pd


start=Gui()
start.form()
if start.sub_button:
    if start.jobtitle:
        if (start.location_type=="Other" and start.location) or start.location_type=="Remote":
            start.searcher()
            start.show()
        else:
            st.warning("Enter a location!!!")
    else:
        st.warning("Enter a job title!!!")