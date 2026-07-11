import yfinance as yf
## we probably do not needs pandas graphing

def getTicker(ticker):
    tickSym = yf.Ticker(ticker)
    data = tickSym.info["currentPrice"]
    return data

