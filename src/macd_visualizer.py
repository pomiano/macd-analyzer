import matplotlib.pyplot as plt

class MACD_visualizer:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def plot_macd(self):
        plt.figure(figsize=(12, 6))

        plt.plot(self.analyzer.date, self.analyzer.macd, label="MACD", color="#1f77b4")

        plt.plot(self.analyzer.date, self.analyzer.signal, label="SIGNAL", color="#FF6F61")

        for i, signal_type in self.analyzer.buy_sell_signals:
            if signal_type == 'Buy':
                plt.scatter(self.analyzer.date[i], self.analyzer.macd[i], color='green', marker='^', zorder=5, s = 70, label='Buy Signal' if i == 0 else "")
            elif signal_type == 'Sell':
               plt.scatter(self.analyzer.date[i], self.analyzer.macd[i], color='red', marker='v', zorder=5, s=70, label='Sell Signal' if i == 0 else "")


        buy_marker = plt.scatter([], [], color='green', marker='^', label='Sygnał zakupu')
        sell_marker = plt.scatter([], [], color='red', marker='v', label='Sygnał sprzedaży')

        plt.title('Wskaźnik MACD - złoto')
        plt.xlabel('Data')
        plt.legend(loc='upper left')

        plt.grid(True)

        tick_interval = 100
        plt.xticks(self.analyzer.date[::100])

        plt.tight_layout()
        plt.show()

    def plot_prices(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.analyzer.date, self.analyzer.data, label="Closing Price", color="black")

        plt.title("Notowania złota")
        plt.xlabel("Data")
        plt.ylabel("Cena(USD)")

        plt.grid(True)

        plt.xticks(self.analyzer.date[::100])
        plt.tight_layout()
        plt.show()


    def plot_prices_with_signals(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.analyzer.date, self.analyzer.data, label="Cena zamknięcia", color="black")

        for index, signal_type in self.analyzer.buy_sell_signals:
            if signal_type == 'Buy':
                plt.scatter(self.analyzer.date[index], self.analyzer.data[index], color='green', marker='^', zorder=5, s = 50)
            elif signal_type == 'Sell':
                plt.scatter(self.analyzer.date[index], self.analyzer.data[index], color='red', marker='v', zorder=5, s = 50)

        buy_marker = plt.scatter([], [], color='green', marker='^', label='Sygnał zakupu')
        sell_marker = plt.scatter([], [], color='red', marker='v', label='Sygnał sprzedaży')

        plt.title("Notowania złota z sygnałami kupna/sprzedaży")
        plt.xlabel("Data")
        plt.ylabel("Cena(USD)")
        plt.legend()
        plt.grid(True)

        plt.xticks(self.analyzer.date[::100])
        plt.tight_layout()
        plt.show()