import streamlit as st
import pandas as pd

st.set_page_config(page_title="Linkedin jobs")
st.title("Results🐧:")
table=pd.read_csv("results.csv")

for index, row in table.iterrows():   #هر سطر در جدولو به صورت دو تایی ایندکس و اون سطر میده
    with st.container(border=True):
        st.markdown(f"### {row['Title']}")
        st.markdown(f"**Company:** {row['Company']}")
        st.markdown(f"**Location:** {row['Location']}")
        st.markdown(f"<a href='{row["Link"]}'> Tap to see the full information! </a>", unsafe_allow_html=True)