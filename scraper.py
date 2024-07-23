# scraper.py

import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = 'http://example.com'

# Fetch the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Print the title of the page
print(soup.title.text)

# Save the title to a CSV file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title"])
    writer.writerow([soup.title.text])

# Modify scraper.py to scrape additional data

    additional_data = soup.find_all('p')

    for data in additional_data:

        writer.writerow([data.text])

