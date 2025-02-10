Web Scraping with Requests, BeautifulSoup, and Requests-HTML

This repository contains Python scripts for retrieving and parsing HTML data using requests, BeautifulSoup, and requests-html.
Files in the Repository
0_retrieving_html.py: Fetches HTML content from Flipkart using requests and saves it to flipkart.html.
1_bs4.py: Parses flipkart.html using BeautifulSoup to extract and display relevant information.
2_requests_html.py: Uses requests-html to retrieve and process JSON data from Python.org.

Requirements
Install the required Python packages before running the scripts:
pip install requests fake-useragent beautifulsoup4 requests-html

Usage
Retrieve HTML Data
Run the following command to fetch the webpage and save it:
python 0_retrieving_html.py

Parse HTML Data
Run the parsing script to extract and display relevant information:
python 1_bs4.py

Fetch JSON Data
Run the requests-html script to fetch JSON data from Python.org:
python 2_requests_html.py


Output
he parsing script extracts:
The title of the page
All <a> tags (links)
The title's string content
The parent tag of the title
The requests-html script fetches and prints JSON data from Python.org






