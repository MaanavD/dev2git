import requests
import argparse
from bs4 import BeautifulSoup
parser = argparse.ArgumentParser()

parser.add_argument('-u', '--url', default='https://devpost.com/software/microscan')

args = parser.parse_args()
URL = args.url

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

finalHeadings = []
finalTexts = []
# Title, subtitle of Project
title = soup.find("h1", attrs={'id': 'app-title'})
title = str(title).strip("<h1 id=\"app-title\">").strip("</")
subtitle = soup.find("p", attrs={'class': "large"})
subtitle = str(subtitle).strip("<p class=\"large\">").strip("</").lstrip().rstrip()

# Heading & Text Parsing

# Image parsing

# Conversion to README.md