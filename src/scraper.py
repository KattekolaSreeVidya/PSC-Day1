# src/scraper.py

import requests
from bs4 import BeautifulSoup
import csv

def fetch_data():
    # URL to scrape
    url = 'http://example.com'

    # Fetch the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the title
    title = soup.title.text

    # Extract additional data
    additional_data = [data.text for data in soup.find_all('p')]

    return (title, additional_data)

def save_to_csv(title, additional_data):
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title"])
        writer.writerow([title])
        for data in additional_data:
            writer.writerow([data])

if __name__ == '__main__':
    title, additional_data = fetch_data()
    save_to_csv(title, additional_data)
