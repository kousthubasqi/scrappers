from scrappers.investingcom import InvestingComScrapper
from scrappers.money_control import MoneyControlScrapper

if __name__ == '__main__':
    # Example usage
    investingcom_scrapper = InvestingComScrapper()
    data = investingcom_scrapper.get_historical_data('995210', '03/04/2020', '03/14/2020')
    print(repr(data[0]))

    # moneycontrol_scrapper = MoneyControlScrapper()
    # data = moneycontrol_scrapper.get_news('recommendations', 2)
    # print(data)