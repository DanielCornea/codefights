import pandas as pd 
from datetime import datetime
# Test data 

#  output[i][0] - local server date in the YYYY-MM-DD format;
#  output[i][1] - a ticker symbol for some instrument;
#  output[i][2] - a string corresponding to the open price;
#  output[i][3] - a string corresponding to the high price;
#  output[i][4] - a string corresponding to the low price;
#  output[i][5] - a string corresponding to the close price.

timestamp = [1450625399,1450625400,	1450625500,1450625550,1451644200,1451690100,1451691000]
instrument = ["HPQ",		"HPQ",	"HPQ",	"HPQ", "AAPL", "HPQ", "GOOG"]
side = 		["sell",	"buy",	"buy",	"sell", "buy", "buy", "buy"]
price =		[10, 20.3, 35.5, 8.65, 20, 10, 100.35]
size = 		[10,1,	2,	3, 5, 1, 10]

timestamp = [datetime.utcfromtimestamp(int(x)) for x in timestamp]

dict = {
    
    "instrument": instrument, 
    "side"      : side, 
    "price"     : price, 
    "size"      : size
}


df = pd.DataFrame(dict, index = timestamp)
dates = [x.date() for x in df.index]

dates = list(set(dates))
dates.sort()
print(dates)


print(df)
# print(df.index.min())
# print(df.loc[df.index.min()]['price'])
output_vector = 
for date in dates : 
    aux = df[df.index.date == date]
    instrs = list(set(aux['instrument']))
    print('--------------------------------')
    for instr in instrs:
        aux2 = aux[aux['instrument'] == instr]
        print(instr + " Opening Price: ", aux2.loc[aux2.index.min()]['price'])
        print(instr + " High Price: ", aux2['price'].max())
        print(instr + " Low Price: ", aux2['price'].min())
        print(instr + " Close Price: ", aux2.loc[aux2.index.max()]['price'])
    print('--------------------------------')