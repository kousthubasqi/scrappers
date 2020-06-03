from scrappers.investingcom import InvestingComScrapper
from scrappers.money_control import MoneyControlScrapper
from scrappers.economictimes import EconomicTimesScrapper
from scrappers.livemint import LiveMintScrapper
from scrappers.cnbctv18 import CNBCTV18Scrapper
from scrappers.ndtv import NDTVScrapper

if __name__ == '__main__':
    # Example usage
    # investingcom_scrapper = InvestingComScrapper()
    # data = investingcom_scrapper.get_historical_data('995210', '03/04/2020', '03/14/2020')
    # print(repr(data[0]))

    # moneycontrol_scrapper = MoneyControlScrapper()
    # url = 'https://www.moneycontrol.com/news/business/stocks/aviation-stocks-tumble-on-no-relief-package-suspension-of-flights-till-may-31-5280941.html'
    # data = moneycontrol_scrapper.get_content_and_keywords(url)
    # print(data)

    # livemint_scrapper = LiveMintScrapper()
    # print(livemint_scrapper.get_news(page=1))

    cnbc_scrapper = CNBCTV18Scrapper ()
    print(cnbc_scrapper.get_news(page=600))

    ndtv_scrapper = NDTVScrapper()
    print(ndtv_scrapper.get_news(page=2))