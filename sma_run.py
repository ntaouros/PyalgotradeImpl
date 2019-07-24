
from __future__ import print_function
import Constants
import sma_crossover
from pyalgotrade import plotter
from pyalgotrade.tools import quandl
from pyalgotrade.stratanalyzer import sharpe


def main(plot):
    instrument = "AAPL"
    smaPeriod = 30

    # Download the bars.
    feed = quandl.build_feed("WIKI", [instrument,"NVDA"], 2016, 2018, Constants.data_directory)

    strategy = sma_crossover.SMACrossOver(feed, instrument, smaPeriod)
    sharpeRatioAnalyzer = sharpe.SharpeRatio()
    strategy.attachAnalyzer(sharpeRatioAnalyzer)
    if plot:
        plt = plotter.StrategyPlotter(strategy, True, True, True)
        plt.getInstrumentSubplot(instrument).addDataSeries("sma", strategy.getSMA())

    strategy.run()

    print("Sharpe ratio: %.2f" % sharpeRatioAnalyzer.getSharpeRatio(0.05))

    if plot:
        plt.plot()


if __name__ == "__main__":
    main(False)
