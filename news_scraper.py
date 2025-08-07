import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

# Send a request to the website
response = requests.get(url)
response_data = response.text

# load the html content into BeautifulSoup
soup = BeautifulSoup(response_data, "html.parser")

# Find all headlines
headlines = soup.find_all(name="h2")

# Open a file to save headlines
with open("headlines.txt","w" ) as file:
    for index, h in enumerate(headlines, start=1):
        text = h.get_text().strip()
        if text:
            file.write(f"{index}. {text}\n")

print("Headlines saved to 'headlines.txt'")