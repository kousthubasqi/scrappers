from bs4 import BeautifulSoup
import urllib3


class InvestingComScrapper:
    headers = {'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def get_historical_data(self, curr_id, st_date, end_date, interval_sec='Daily', sort_col='date', sort_ord= 'DESC', action='historical_data'):
        url = 'https://www.investing.com/instruments/HistoricalDataAjax'

        data = {
            'curr_id': curr_id,
            'st_date': st_date,
            'end_date': end_date,
            'interval_sec': interval_sec,
            'sort_col': sort_col,
            'sort_ord': sort_ord,
            'action': action
        }

        http = urllib3.PoolManager()
        r = http.request('POST', url, fields=data, headers=self.headers)
        soup = BeautifulSoup(r.data, features='html.parser')
        table = soup.find('tbody').find_all('tr')
        rows = []
        for row in table:
            cells = row.find_all('td')
            cells = map(lambda r: r.text, cells)
            cells = list(cells)
            rows.append(cells)
        return rows

