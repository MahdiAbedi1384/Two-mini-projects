"extract houses data from Divar"
from bs4 import BeautifulSoup
import requests
from pathlib import Path
import json

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

# request to divar.ir and extract response content
url = 'https://divar.ir/s/nur/buy-villa'

response_text = requests.get(url,headers=headers).text

soup = BeautifulSoup(response_text, 'html.parser')

# create a dictionary to dump in json file
dictionary = dict()

# a label for count cards
post_number = 1

# find all tags with specific class
main_tags = soup.find_all('div', class_='full-width-widget-col-c8bd0')

# use loop for get cards data and add into dictionary
for tag in main_tags:

    title = tag.find('h2', class_='unsafe-kt-post-card__title')

    price = tag.find('div', class_='unsafe-kt-post-card__description')

    more_info = tag.find('a', class_='unsafe-kt-post-card__action')

    advertiser = tag.find('span', class_='unsafe-kt-post-card__bottom-description kt-text-truncate')

    img = tag.find('img',
    class_='kt-image-block__image kt-image-block__image--fading kt-image-block__image--lazy-loaded')

    dictionary[post_number] = {
            'title': title.text if title else None,
            'price': price.text if price else None,
            'more_info':f'https://divar.ir{more_info['href'] if more_info and more_info.has_attr('href') else None}' ,
            'advertiser': advertiser.text if advertiser else None,
            'img': img['src'] if img and img.has_attr('src') else None
        }

    post_number += 1


# open a file and dump dictionary into it
with Path('data.json').open('w', encoding='utf-8') as f:

    json.dump(dictionary, f, ensure_ascii=False,sort_keys=True, indent=4)

