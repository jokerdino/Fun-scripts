import pandas as pd

data = pd.read_csv('input.csv')

data['amount'] = data['quantity'] * data['price']

# company, transaction type, date, cost per share, shares, amount
data = data[['symbol', 'trade_type', 'trade_date', 'price', 'quantity','amount']]

data = data.set_axis(["Company", "Transaction Type", "Date", "Cost per share", "Shares", "Amount"],axis=1,inplace=False)

data.to_excel("output.xlsx",index=False)
