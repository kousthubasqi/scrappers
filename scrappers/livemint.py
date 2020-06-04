import requests
import re
from bs4 import BeautifulSoup

class LiveMintScrapper:
    """A scrapper for moneycontrol.com"""

    site = 'https://www.livemint.com'

    def get_news(self, page=0):
        """Get news titles and links for a given section and page"""

        path = '/listing/section/companies/{}'.format(page)

        url = self.site + path
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        news_list = soup.find('div', {'itemtype': 'http://schema.org/ItemList'})

        news_list = news_list.find_all('span', {'itemprop': 'itemListElement'})
        
        results = []

        for news_item in news_list:
            title = news_item.find('meta', {'itemprop': 'name'})['content']
            link = news_item.find('meta', {'itemprop': 'url'})['content']
            date_published = news_item.find('span', {'class': 'articleInfo pubtime'})
            date_published = date_published.find('span', {'data-sectionname': 'Companies'})['data-updatedlongtime']

            result = {
                'title': title,
                'date_time': date_published,
                'link': link
            }

            results.append(result)

        return results

    def get_news_content(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        content_sec = soup.find('div', {'class': 'contentSec'})
        content = content_sec.text
        m = re.match(r'([.\s\S]+)Subscribe to newsletters[.\s\S]+', content)
        if m is not None:
            return m[1]
        else:
            return content


