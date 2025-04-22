from data.y_finance_collector import yFinanceCollector

if __name__ == "__main__":
    _yf = yFinanceCollector({
        'advantage_url':'https://www.alphavantage.co/query?function=OVERVIEW&symbol=_ticker}&apikey=_api_key'
        , 'advantage_key': 'HVT22YLBMRKMN92D'
    })

    res = _yf.get_historical_data('AAPL')

    print(res)

