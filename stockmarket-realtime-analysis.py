import yfinance as yf


if __name__ == "__main__":
    apple_stock = yf.download("MSFT", start="2025-01-03",end="2025-04-23")
    print(apple_stock)
    pass
