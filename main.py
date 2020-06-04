from scrappers.investingcom import InvestingComScrapper
from scrappers.money_control import MoneyControlScrapper
from scrappers.economictimes import EconomicTimesScrapper
from scrappers.livemint import LiveMintScrapper
from scrappers.cnbctv18 import CNBCTV18Scrapper
from scrappers.ndtv import NDTVScrapper
from scrappers.businessline import BusinessLineScrapper

if __name__ == '__main__':
    # Example usage
    # investingcom_scrapper = InvestingComScrapper()
    # data = investingcom_scrapper.get_historical_data('995210', '03/04/2020', '03/14/2020')
    # print(repr(data[0]))

    # moneycontrol_scrapper = MoneyControlScrapper()
    # url = 'https://www.moneycontrol.com/news/business/stocks/aviation-stocks-tumble-on-no-relief-package-suspension-of-flights-till-may-31-5280941.html'
    # data = moneycontrol_scrapper.get_content_and_keywords(url)
    # print(data)

    # et = EconomicTimesScrapper()
    # # print(et.get_news(page=2))
    # print(et.get_news_content('https://economictimes.indiatimes.com/markets/stocks/news/shanghai-shares-end-lower-on-simmering-us-china-trade-tensions/articleshow/76192569.cms'))
    

    # livemint_scrapper = LiveMintScrapper()
    # print(livemint_scrapper.get_news(page=1))
    # livemint_scrapper.get_news_content('https://www.livemint.com/companies/people/ratan-tata-expressed-shock-over-elephant-killing-in-kerala-says-justice-need-to-prevail-11591207995838.html')

    cnbc_scrapper = CNBCTV18Scrapper ()
    print(cnbc_scrapper.get_news_content(cnbc_scrapper.get_news(page=300)[5]['link']))

    # ndtv_scrapper = NDTVScrapper()
    # # print(ndtv_scrapper.get_news(page=2))
    # print(ndtv_scrapper.get_news_content('https://www.ndtv.com/business/gold-price-today-3-june-2020-gold-futures-ease-to-rs-46-650-10-grams-as-equities-jump-amid-covid-19-2239222'))

    # bs = BusinessLineScrapper()
    # print(bs.get_news_content(bs.get_news(page=2)[7]['link']))
