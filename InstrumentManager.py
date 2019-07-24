from __future__ import print_function

class InstrumentManager():
    def __init__(self, feed, instrument):
        self.instrument = instrument
        self.__prices = feed[instrument].getPriceDataSeries()
        self.__signal = None

    #TODO add logic for buy sell signals
    # idea: Maybe just add a get bar and implement the logic on the actual strategy
    def onBars(self, bars):
        bar= bars.getBar(self.instrument)
        print(bar)
        return True



