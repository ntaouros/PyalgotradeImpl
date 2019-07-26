from pyalgotrade import strategy

class MultipleInstrumentStrategy(strategy.BacktestingStrategy):


    def __init__(self, feed, instruments):
        super(MultipleInstrumentStrategy, self).__init__(feed)
        self.__position = []
        self.__feed = feed
        self.__instruments = instruments

    def onBars(self, bars):
        for instr in self.__instruments:
            prices = self.__feed[instr].getPriceDataSeries()
            if prices.__len__() > 5 :
                price = bars.getBar(instr).getPrice()
                print("Current", price,"Previous", prices[-1-1]) # prices[-1-1] gets the yesterday's price
        True