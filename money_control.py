import requests
import re
from bs4 import BeautifulSoup

class MoneyControlScrapper:
    """A scrapper for moneycontrol.com"""

    site = 'https://www.moneycontrol.com'

    def get_latest_sentiments(self):
        """Get the latest community sentiments"""

        path = '/techmvc/ajaxcontent/community_sentimeter_data_ajax/broker_research/false/community_most_active1'
        url = self.site + path

        r = requests.get(url)

        soup = BeautifulSoup(r.text)
        sentiment_list = soup.find_all('li')

        result_list = []

        for sentiment in sentiment_list:
            company_name = str(sentiment.find('p', {'class': 'txt14_333B'}).text)

            buy_sell = sentiment.find('p', {'class': 'txt13_bold'})
            buy = buy_sell.find('span', {'class': 'green'}).text
            sell = buy_sell.find('span', {'class': 'red'}).text


            b = int(re.search(r'Buy (.+)%', buy).group(1))
            s = int(re.search(r'Sell (.+)%', sell).group(1))
            h = 100 - b - s

            result = {
                "company_name": company_name,
                "buy": b,
                "sell": s,
                "hold": h
            }
            result_list.append(result)
        
        return result_list

# Example usage
scrapper = MoneyControlScrapper()
data = scrapper.get_latest_sentiments()
print(data)