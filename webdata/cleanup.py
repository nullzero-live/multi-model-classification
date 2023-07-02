import csv
import requests
from bs4 import BeautifulSoup
import os

# Create the data_output directory if it does not already exist
if not os.path.exists('output'):
    os.makedirs('output')

counter = 0

with open('links.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        url = row[0]
        response = requests.get(url)

        # Check if response object is not None
        if response is not None:
            soup = BeautifulSoup(response.content, 'html.parser')
            main_tag = soup.find('main', id='main-content', class_='bd-main')
            if main_tag is not None:
                main_text = main_tag.get_text(separator='\n', strip=True)

                # Create a filename based on the url
                filename = url.replace('https://', '').replace('http://', '').replace('/', '_').replace(':', '') + '.txt'

                # Save the text to a file in the data_output directory
                with open('output/' + filename, 'w') as f:
                    print(counter)
                    counter += 1
                    f.write(main_text)
            else:
                print(f"No main tag found in {url}")
        else:
            print(f"Error fetching {url}")