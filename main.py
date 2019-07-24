from pyalgotrade.tools import quandl
from MultipleInstrumentStrategy import MultipleInstrumentStrategy
import Constants

def main():
    instruments = ["AAPL", "NVDA"]
    feed = quandl.build_feed("WIKI", instruments, 2016, 2018, Constants.data_directory)
    strategy = MultipleInstrumentStrategy(feed, instruments)
    strategy.run()

main()