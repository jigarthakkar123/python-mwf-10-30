stocks = ['GEEKS', 'For', 'geeks']
prices = [2175, 1127, 2750]
 
new_dict = {stocks: prices for stocks,prices in zip(stocks, prices)}
print(new_dict)
