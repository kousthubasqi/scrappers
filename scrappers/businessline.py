import requests
import re
from bs4 import BeautifulSoup

class BusinessLineScrapper:
    """A scrapper for thehindubusinessline.com"""

    site = 'https://www.thehindubusinessline.com'

    def get_news(self, page=3):
        """Get news titles and links for a given section and page"""

        path = '/markets/stock-markets/?page={}'.format(page)

        url = self.site + path
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        news_list = soup.find_all('article')
        results = []

        for news_item in news_list:
            As = news_item.find_all('a')
            a = As[0]
            title = a.text
            link = a['href']

            result = {
                'title': title,
                'link': link
            }

            results.append(result)
        

        return results

    def get_news_content(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        content_sec = soup.find('div', {'class': 'paywall'})
        content = content_sec.text
        return content
