ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

volatility = []
for row in ohlc[1:]:
    volatility.append(row[1] - row[2])

print(volatility)

# volatility = []
# for row in range(1. len(ohic)):
    # volatility.append(ohlc[row][1] - ohlc[row][2])

# print(volatility)