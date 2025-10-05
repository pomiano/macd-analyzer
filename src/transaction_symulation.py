import matplotlib.pyplot as plt

class Transaction_symulation:
    def __init__(self,analyzer, initial_capital = 1000):
        self.analyzer = analyzer
        self.asset_quantity = 0
        self.initial_cash_capital = initial_capital * self.analyzer.data[0]
        self.cash_capital = initial_capital * self.analyzer.data[0]
        self.transactions = []
        self.portfolio_value = []

    def simulate_trading(self):
        for signal in self.analyzer.buy_sell_signals:
            if signal[1] == 'Sell' and self.asset_quantity > 0 :
                sell_price = self.analyzer.data[signal[0]]
                date = self.analyzer.date[signal[0]]
                self.cash_capital = self.asset_quantity * sell_price
                self.asset_quantity = 0
                self.transactions.append({
                    'date': date,
                    'type': 'Sell',
                    'price': sell_price,
                    'asset_quantity': self.asset_quantity,
                    'total_cash': self.cash_capital
                })

            elif signal[1] == 'Buy' and self.cash_capital > 0:
                buy_price = self.analyzer.data[signal[0]]
                date = self.analyzer.date[signal[0]]
                self.asset_quantity = self.cash_capital / buy_price
                self.cash_capital -= self.asset_quantity * buy_price
                self.transactions.append({
                    'date': date,
                    'type': 'Buy',
                    'price': buy_price,
                    'asset_quantity': self.asset_quantity,
                    'total_cash': self.cash_capital
                })

    def print_statistics(self):
        print(f"Initial cash capital: {self.initial_cash_capital}")
        print(f"Capital: {self.asset_quantity}")
        print(f"Cash: {self.cash_capital}")
        print("\nTransactions:")
        for index, transaction in enumerate(self.transactions, start=1):
            print(
                f"{index}. {transaction['type']} - Date: {transaction['date']}, Price: {transaction['price']}, "
                f"Asset quantity: {transaction['asset_quantity']}, Total_cash: {transaction['total_cash']}"
            )

        favorable = 0
        unfavorable = 0
        print("\nBuy/Sell Signal Analysis Results:")
        for i in range(0, len(self.analyzer.buy_sell_signals) - 1, 2):     # Iterujemy po wszystkich oprócz ostatniego
            first_index, first_type = self.analyzer.buy_sell_signals[i]
            second_index, second_type = self.analyzer.buy_sell_signals[i +1]
            if self.analyzer.data[first_index] < self.analyzer.data[second_index]:
                favorable+=1
                print("favorable:")
                print(self.analyzer.data[first_index], self.analyzer.data[second_index])
            else:
                unfavorable+=1
                print("unfavorable:")
                print(self.analyzer.data[first_index], self.analyzer.data[second_index], )
        print(f"Favorable: {favorable}")

        print(f"Unfavorable: {unfavorable}")



    def plot_cash_flow(self):
        dates = [t["date"] for t in self.transactions]
        cash_values = [t["total_cash"] for t in self.transactions]

        plt.figure(figsize=(12, 6))
        plt.plot(dates, cash_values, marker='o', linestyle='-', color='blue', label="Cash Balance")

        plt.title("Cash Flow Over Time")
        plt.xlabel("Date")
        plt.ylabel("Cash Balance")
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.show()

    def calculate_portfolio_value(self):
        k = 0
        bought = False;
        min =float('inf')
        max = 0
        current_asset_quantity = 0
        portfolio_value = [None] * len(self.analyzer.date)
        portfolio_value[0] = self.initial_cash_capital
        for i in range(1,len(self.analyzer.date)):
            price = self.analyzer.data[i]
            if k < len(self.analyzer.buy_sell_signals) and self.analyzer.buy_sell_signals[k][0] == i and k!=len(self.analyzer.buy_sell_signals)-1:
                if self.analyzer.buy_sell_signals[k][1] == 'Sell' and bought == True:
                    bought = False
                    portfolio_value[i] = current_asset_quantity * self.analyzer.data[i]
                elif self.analyzer.buy_sell_signals[k][1] == 'Buy':
                    bought = True
                    current_asset_quantity = portfolio_value[i-1]/self.analyzer.data[i]
                    portfolio_value[i] = current_asset_quantity * self.analyzer.data[i]
                k+=1
            else:
                if bought == True:
                    portfolio_value[i] = current_asset_quantity * self.analyzer.data[i]
                elif bought == False:
                    portfolio_value[i] = portfolio_value[i-1]
            if portfolio_value[i] > max:
                max = portfolio_value[i]
            elif portfolio_value[i] < min:
                min = portfolio_value[i]

        print(f"Portfolio value - MIN: {min}, MAX: {max}")
        self.portfolio_value = portfolio_value

    def plot_portfolio_value(self, start_day=0):
        self.calculate_portfolio_value()
        if start_day < 0 or start_day >= len(self.portfolio_value):
            print("Invalid start day!")
            return

        plt.figure(figsize=(12, 6))
        plt.plot(self.analyzer.date[start_day:], self.portfolio_value[start_day:], label="Kapitał",
                 color="blue")

        for i, signal_type in self.analyzer.buy_sell_signals:
            if signal_type == 'Buy':
                plt.scatter(self.analyzer.date[i], self.portfolio_value[i], color='green', marker='^', zorder=5, label='Buy Signal' if i == 0 else "")
            elif signal_type == 'Sell':
                plt.scatter(self.analyzer.date[i], self.portfolio_value[i], color='red', marker='v', zorder=5, label='Sell Signal' if i == 0 else "")

        buy_marker = plt.scatter([], [], color='green', marker='^', label='Sygnał zakupu')
        sell_marker = plt.scatter([], [], color='red', marker='v', label='Sygnał sprzedaży')

        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:,.0f}'))

        plt.axhline(y=self.initial_cash_capital, color='red', linestyle='--', linewidth=1, label = 'Kapitał początkowy')

        plt.title("Symulacja transakcji - złoto")
        plt.xlabel("Data")
        plt.ylabel("Kapitał(USD)")
        plt.legend()
        plt.grid(True)


        tick_interval = 100
        plt.xticks(self.analyzer.date[::tick_interval])
        plt.tight_layout()
        plt.show()



