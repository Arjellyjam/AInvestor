import yfinance as yf
## we probably do not needs pandas graphing

def getTicker(ticker):
    tickSym = yf.Ticker(ticker)
    info = tickSym.info
    data = {
        "currentPrice": info.get("currentPrice", "N/A"),
        "Forward P/E": info.get("forwardPE", "N/A"),
        "Trailing P/E": info.get("trailingPE", "N/A"),
        "Debt to Equity": info.get("debtToEquity", "N/A"),
        "Return on Equity": info.get("returnOnEquity", "N/A"),
        "Operating Margin": info.get("operatingMargins", "N/A"),
        "Revenue Growth": info.get("revenueGrowth", "N/A"),
        "Analyst Target": info.get("targetMeanPrice", "N/A"),
        "Analyst Rating": info.get("recommendationKey", "N/A")
    }
    return data

