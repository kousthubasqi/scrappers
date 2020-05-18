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

        soup = BeautifulSoup(r.text, 'html.parser')
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

    def get_all_stocks(self):
        path = '/india/stockpricequote/'
        url = self.site + path

        r = requests.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')
        stock_table = soup.find('table', 'pcq_tbl MT10')
        stock_links = stock_table.find_all('a')

        result = list(map(lambda x: {'symbol': x['title'], 'link': x['href']}, stock_links))

        return result

    def get_community_sentiments_for_stock(self, url):
        """Get the community sentiments for a stock
        Neet to provide URL right now and there isn't a workaround as the path
        is in weird format like 
            https://www.moneycontrol.com/india/stockpricequote/paintsvarnishes/asianpaints/AP31
        Hence use function get_all_stocks to first get the link map for all stocks    
        """

        r = requests.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')
        buy_span = soup.find('span', 'bullet_clr buy buy_results')
        sell_span = soup.find('span', 'bullet_clr sell sell_results')
        hold_span = soup.find('span', 'bullet_clr hold hold_results')

        buy = buy_span['result']
        sell = sell_span['result']
        hold = hold_span['result']
        
        result = {
            'buy': buy,
            'sell': sell,
            'hold': hold
        }

        return result
    
    def get_community_sentiments_for_all(self):
        stock_list = self.get_all_stocks()

        result = []
        for stock in stock_list:
            try:
                sentiment = self.get_community_sentiments_for_stock(stock['link'])
            except:
                sentiment = 'Sentiment not available'
            print(stock['symbol'], sentiment)
            result.append({'symbol': stock['symbol'], 'sentiment': sentiment})

        return result

    def get_news(self, section, page=1):
        """Get news titles and links for a given section and page"""

        if section == 'stock':
            path = '/news/business/stocks/page-' 
        elif section == 'business':
            path = '/news/business/page-'
        elif section == 'recommendations':
            path = '/news/tags/recommendations.html/page-'
        else:
            raise ValueError('This section is currently not supported')

        url = self.site + path + str(page) + '/'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        news_section = soup.find('ul', {'id': 'cagetory'})

        news_list = news_section.find_all('li')
        
        result_list = []
        for news in news_list:
            try:
                date_span = news.find('span')
                date_time = date_span.text if date_span != None else ''
                a = news.find('a')
                title = a['title']
                link = a['href']

                result = {
                    'date_time': date_time,
                    'title': title,
                    'link': link
                }
                result_list.append(result)
            except Exception:
                pass

        return result_list
        
        # An API for mc - https://priceapi-aws.moneycontrol.com/pricefeed/bse/equitycash/NTP
