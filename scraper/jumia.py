import requests
# import aiohttp
# import asyncio
from bs4 import BeautifulSoup


def jumia_scraper_bot(key):
    link = "https://www.jumia.ng"
    url = "https://www.jumia.ng/catalog/?q=" + key

    reponse_page = requests.get(url)

    page_web = BeautifulSoup(reponse_page.content, 'html.parser')

    articles = page_web.find_all(
        'article', attrs={'class': 'prd _fb col c-prd'})

    items = []
    for article in articles:
        item = {}
        item['link'] = link + article.find('a')['href']
        item['image'] = article.find('img')['data-src']
        item['title'] = article.find('h3', attrs={'class': 'name'}).text
        item['price'] = article.find('div', attrs={'class': 'prc'}).text
        item['from'] = 'jumia'
        if item['price']:
            items.append(item)

    return items


# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()


# async def jumia_scraper_bot_async(key):
#     link = "https://www.jumia.ng"
#     url = "https://www.jumia.ng/catalog/?q=" + key

#     async with aiohttp.ClientSession() as session:
#         reponse_page = await fetch(session, url)

#         page_web = BeautifulSoup(reponse_page, 'html.parser')

#         articles = page_web.find_all(
#             'article', attrs={'class': 'prd _fb col c-prd'})

#         items = []
#         for article in articles:
#             item = {}
#             item['link'] = link + article.find('a')['href']
#             item['image'] = article.find('img')['data-src']
#             item['title'] = article.find('h3', attrs={'class': 'name'}).text
#             item['price'] = article.find('div', attrs={'class': 'prc'}).text
#             item['from'] = 'jumia'
#             if item['price']:
#                 items.append(item)

#         return items


if __name__ == '__main__':
    jumia_scraper_bot('computer')
