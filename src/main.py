import pandas as pd

from macd_analyzer import MACD_analyzer
from macd_visualizer import MACD_visualizer
from transaction_symulation import Transaction_symulation

file = pd.read_csv('zloto2022.csv')

data = file['Zamkniecie'].tolist()
date = file['Data'].tolist()


gold_analyzer = MACD_analyzer(data, date)

macd = gold_analyzer.calculate_macd()
signal = gold_analyzer.calculate_signal()
signals = gold_analyzer.detect_crossovers()

visualizer = MACD_visualizer(gold_analyzer)
visualizer.plot_prices()
visualizer.plot_macd()
visualizer.plot_prices_with_signals()

symulation = Transaction_symulation(gold_analyzer)
symulation.simulate_trading()
symulation.print_statistics()
symulation.plot_portfolio_value()






