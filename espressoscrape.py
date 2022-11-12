import requests
from bs4 import BeautifulSoup

# Send GET request to URL
response = requests.get('https://au.espres.so/blogs/blog/')

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all anchor tags (links)
links = soup.find_all('a')
links = [link.get('href') for link in links]

# Loop through links
for link in links:
    if link is not None:
        # Add prefix if needed then print results
        if link.startswith('/'):
            link = 'https://au.espres.so' + link
        print(link)
