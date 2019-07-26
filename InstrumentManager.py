from __future__ import print_function
#TODO maybe useless. or I can add a paramater for how many consecutive days the price has been going up or down for momentum purposes
class InstrumentManager():
    def __init__(self, feed, instrument):
        self.instrument = instrument
        self.__prices = feed[instrument].getPriceDataSeries()
        self.__signal = None

    #TODO add logic for buy sell signals
    # idea: Maybe just add a get bar and implement the logic on the actual strategy
    def getPrice(self, bars):
        # print (bars.items())
        # print("GetPrice -> ",bars.getBar(self.instrument).getPrice() )
        # print("ClosePrice -> ",bars.getBar(self.instrument).getClose() )

        return bars.getBar(self.instrument).getPrice()



