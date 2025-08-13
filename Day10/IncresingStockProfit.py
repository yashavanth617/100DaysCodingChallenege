def StockProfit(arr):
    max_profit = 0
    buy_price = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < buy_price:
            buy_price = arr[i]
        else:
            profit = arr[i] - buy_price
            max_profit = max(max_profit, profit)
    
    print(max_profit)

arr = [7,1,5,3,6,4]
StockProfit(arr)
