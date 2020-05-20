import requests
import re
from bs4 import BeautifulSoup

class EconomicTimesScrapper:
    """A scrapper for moneycontrol.com"""

    site = 'https://economictimes.indiatimes.com/'

    def get_news(self, page=0):
        """Get news titles and links for a given section and page"""

        path = '/lazyloadlistnew.cms?msid=2146843&curpg={}&img=0'.format(page)

        url = self.site + path #+ str(page)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        stories = soup.find_all('div', {'class': 'eachStory'})

        results = []

        for story in stories:
            title = story.find('h3').find('a')
            link = self.site + title['href']
            title = title.text
            date = story.find('time')['data-time']

            result = {
                'title': title,
                'date': date,
                'link': link
            }

            results.append(result)

        return results

