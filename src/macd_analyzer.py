
class MACD_analyzer:
    def __init__(self, data, date):
        self.data = data
        self.date = date
        self.macd = []
        self.signal = []
        self.buy_sell_signals = []

    def calculate_ema(self, N, source_data):
        alfa = 2 / (N + 1)
        ema = []

        for i in range(len(source_data)):
            if i < N:
                ema.append(None)
                continue;
            if source_data[i - N] == None:
                ema.append(None)
                continue;

            ema_value = 0
            deminator_sum = 0

            for j in range(0, N + 1):
                ema_value += (1 - alfa) ** j * source_data[i - j]
                deminator_sum += (1 - alfa) ** j

            ema_value = ema_value / deminator_sum
            ema.append(ema_value)

        return ema

    def calculate_macd(self):
        ema_12 = self.calculate_ema(12, self.data)
        ema_26 = self.calculate_ema(26, self.data)

        macd = []

        for i in range(len(self.data)):
            if (i >= 26):
                macd_value = ema_12[i] - ema_26[i]
                macd.append(macd_value)
            else:
                macd.append(None)
                continue

        self.macd = macd
        return macd

    def calculate_signal(self):
        signal = self.calculate_ema(9, self.macd)
        self.signal = signal
        return signal

    def detect_crossovers(self):
        signals = []
        for i in range(1, len(self.macd)):
            if (self.macd[i - 1] == None) or (self.signal[i - 1] == None):
                continue

            if self.macd[i - 1] < self.signal[i - 1] and self.macd[i] > self.signal[i]:
                signals.append((i, 'Buy'))
            elif self.macd[i - 1] > self.signal[i - 1] and self.macd[i] < self.signal[i]:
                signals.append((i, 'Sell'))

        if signals[0][1] == 'Sell':
            signals.pop(0)


        self.buy_sell_signals = signals
        return signals

