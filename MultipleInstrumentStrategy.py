from pyalgotrade import strategy

class MultipleInstrumentStrategy(strategy.BacktestingStrategy):


    def __init__(self, feed, instruments):
        super(MultipleInstrumentStrategy, self).__init__(feed)
        # self.__position = []
        self.__position = None
        self.__feed = feed
        self.__instruments = instruments

    def onBars(self, bars):
        for instr in self.__instruments:
            prices = self.__feed[instr].getPriceDataSeries()
            bar = bars.getBar(instr)
            if prices.__len__() > 5 and bar is not None :
                price = bar.getPrice()
                date = bar.getDateTime()
                # print(instr,"Current", price,"Previous", prices[-1-1]) # prices[-1-1] gets the yesterday's price
                yesterdayPrice = prices[-1-1]
                buyCondition = price >= yesterdayPrice
                sellCondition = price <= yesterdayPrice
                decideTransaction(self, buyCondition, sellCondition, price, date,instr)

#TODO: Move it to another file
#TODO: Implement multi position (replace __posiition = none with [])
def decideTransaction(strategy, buyCondition, sellCondition, price, date, instr):
    if buyCondition:
        strategy.getLogger().info("%s: BUY [%s] at $%.2f" % (date, instr, price))
    elif sellCondition: # There was a check on  wether the exit order was active or not
        strategy.getLogger().info("%s: SELL [%s] at $%.2f" % (date, instr, price))

