# Imports
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

# Constants
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
PAGES_TO_GET = 1
FILENAME = "csv/NEWS.csv" 

# Initialize an empty list to store the scraped data
upperframe = []

# Open the file before the loop
with open(FILENAME, "w", encoding='utf-8', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write headers to the CSV file
    csv_writer.writerow(['Statement', 'Link', 'Date', 'Source', 'Label'])

    for page in range(1, PAGES_TO_GET + 1):
        print('processing page:', page)
        url = 'https://www.politifact.com/factchecks/list/?page=' + str(page)
        print(url)

        # Use try-except block to handle exceptions
        try:
            # Use the browser to get the url
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()  # Raise an HTTPError for bad responses.

        except requests.exceptions.RequestException as e:
            print(f'Error requesting URL {url}: {e}')
            continue  # Ignore this page. Abandon this and go back.

        soup = BeautifulSoup(response.text, 'html.parser')
        frame = []

        # Find all elements with the class 'o-listicle__item'
        links = soup.find_all('li', attrs={'class': 'o-listicle__item'})

        for j in links:
            Statement = j.find("div", attrs={'class': 'm-statement__quote'}).text.strip()
            Link = "https://www.politifact.com" + j.find("div", attrs={'class': 'm-statement__quote'}).find('a')['href'].strip()
            Date = j.find('div', attrs={'class': 'm-statement__body'}).find('footer').text[-14:-1].strip()
            Source = j.find('div', attrs={'class': 'm-statement__meta'}).find('a').text.strip()
            Label = j.find('div', attrs={'class': 'm-statement__content'}).find('img',
                                                                                 attrs={'class': 'c-image__original'}).get('alt').strip()
            frame.append((Statement, Link, Date, Source, Label))
            
            # Write the row to the CSV file
            csv_writer.writerow([Statement, Link, Date, Source, Label])

    upperframe.extend(frame)

# Create a DataFrame from the scraped data
data = pd.DataFrame(upperframe, columns=['Statement', 'Link', 'Date', 'Source', 'Label'])
