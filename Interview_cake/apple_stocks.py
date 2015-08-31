#Applestocks

stockPricesYesterday = [random.randint(1,100) for _ in xrange(1000)]

ArrSize = len(stockPricesYesterday)
max_delta = 0
for buy_i in xrange(ArrSize):
    for sell_i in xrange(buy_i, ArrSize):
        current_delta = stockPricesYesterday[buy_i] - stockPricesYesterday[sell_i]
        if current_delta > max_delta: max_delta = current_delta

max_delta


buy = 0
sell = 0 
for px in stockPricesYesterday:
    if px < buy: 
        buy = px
    if px > buy: 
        sell = px
    delta = buy - sell
    if max_delta < delta:
        max_delta = buy - sell
max_delta