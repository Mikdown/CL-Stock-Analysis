
def stock_symbol():
    import pandas as pd

    symbols = ['AAPL', 'AMD', 'AMZN', 'CSCO', 'META', 'MSFT', 'NFLX', 'QCOM', 'SBUX', 'TSLA']

    symbol = input("Please enter one of the following symbols!" + str(symbols) + '\n').upper()
    for _ in range(3):
        try:
            df = pd.read_csv('/Users/miked/Downloads/HistoricalData_' + symbol + '.csv')
            df['Symbol'] = symbol
            df['Open'] = df['Open'].str.replace("$", '', regex=True).astype(float)
            df['High'] = df['High'].str.replace("$", '', regex=True).astype(float)
            df['Low'] = df['Low'].str.replace("$", '', regex=True).astype(float)
            df['Close/Last'] = df['Close/Last'].str.replace("$", '', regex=True).astype(float)
            df.rename(columns={'Close/Last': 'Close'}, inplace=True)
            df['Date']= pd.to_datetime(df['Date'])
            print(df)
            df2 = df['Open'].mean()
            print(df2)

        except FileNotFoundError:
            print("You have entered an invalid symbol! Please try again.")
            stock_symbol()
    
    print("Function terminates after 3 invalid entries.")
    return df
    
    
    

