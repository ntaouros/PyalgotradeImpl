from pyalgotrade import strategy
from InstrumentManager import InstrumentManager

class MultipleInstrumentStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instruments):
        super(MultipleInstrumentStrategy, self).__init__(feed)
        self.__position = []
        self.__feed = feed
        self.__instruments = instruments
        self.instManagers = {}
        self.loadInstManagers()

    def loadInstManagers(self):
        for instrument in self.__instruments:
            instrumentManager = InstrumentManager(self.__feed, instrument)
            print(instrument)
            self.instManagers[instrument] = instrumentManager

    def onBars(self,bars):
        print(self.instManagers["AAPL"].onBars(bars))
        True