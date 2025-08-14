# LinkedIn Job Scraper

## Description
This is a Python-based mini project that allows you to scrape jobs from LinkedIn. It uses Selenium to navigate LinkedIn, extract job details, and save the results to a CSV file.Also uses Streamlit to provide a simple user interface for viewing the results. The scraper uses Firefox as the browser backend.

---

## Features
- Scrape jobs from LinkedIn based on:
  - Job title
  - Location
  - Number of results to retrieve
- Extract key job details:
  - Title
  - Company
  - Location
  - Date posted
  - Job link
  - Company logo
- Save the scraped data to a CSV file.
- Streamlit UI to view results in a simple and interactive way.
- Headless scraping with Firefox (no browser window needed).

---

## Requirements
- Python 3.7+
- [Selenium]
- [pandas]
- [Streamlit]
- Firefox browser
- [Geckodriver] installed and added to your PATH

Install dependencies using pip:

```bash
pip install selenium pandas streamlit
```

How to use:
1-Open terminal in project folder
2-Run streamlit app 
```bash
streamlit run R.py
```


