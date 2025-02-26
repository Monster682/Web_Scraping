from bs4 import BeautifulSoup
import requests

# URL to scrape
url = "https://example.com"

# Fetch the page
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract and print all links
for link in soup.find_all("a"):
    print(link.get("href"))
