import requests
import re
from bs4 import BeautifulSoup

class CNBCTV18Scrapper:
    """A scrapper for cnbctv18.com"""

    site = 'https://www.cnbctv18.com'

    def get_news(self, page=3):
        """Get news titles and links for a given section and page"""

        path = '/market/stocks/page-{}/'.format(page)

        url = self.site + path
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        news_list = soup.find_all('div', {'class': 'image-holder PR'})
        
        results = []

        for news_item in news_list:
            a = news_item.find('a')
            title = a['title']
            link = a['href']

            result = {
                'title': title,
                'link': link
            }

            results.append(result)
        

        return results

