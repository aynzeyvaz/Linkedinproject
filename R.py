from job_scraper import linkedin
from streamlit_part import Gui
import streamlit as st
import pandas as pd


start=Gui()
start.form()
if start.sub_button:
    start.searcher()
    start.show()