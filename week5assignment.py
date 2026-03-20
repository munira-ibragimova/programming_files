from abc import ABC, abstractmethod
class Exchanger(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def exchange(self, value):
        pass
    def describe(self, value):
        return f"{self.name}: {value} -> {self.exchange(value)}"

class USDToEUR(Exchanger):
    def __init__(self):
        self.name = "USDToEUR"
    def exchange(self, value):
        return round(value * 0.9216, 2)
class USDToGBP(Exchanger):
    def __init__(self):
        self.name = "USDToGBP"
    def exchange(self, value):
        return round(value * 0.7893, 2)
class USDToJPY(Exchanger):
    def __init__(self):
        self.name = "USDToJPY"
    def exchange(self, value):
        return round(value * 149.52, 2)
class CustomExchanger:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
    def exchange(self, value):
        return round(value * self.rate, 2)
    def describe(self, value):
        return f"{self.name}: {value} -> {self.exchange(value)}"
class ExchangeLog:
    def __init__(self):
        self.entries = []
    def record(self, exchange_name, original, exchanged):
        self.entries.append(f"{exchange_name}: {original} -> {exchanged}")
    def show(self):
        for entry in self.entries:
            print(entry)
class ExchangeDesk:
    def __init__(self, name):
        self.name = name
        self.exchangers = []
        self.exchange_log = ExchangeLog()
    def add_exchanger(self, exchanger):
        self.exchangers.append(exchanger)
    def exchange_all(self, value):
        print(f"=== {self.name} ===")
        for entry in self.exchangers:
            self.exchange_log.record(entry.name, value, entry.exchange(value))
            print(entry.describe(value))
    def show_log(self):
        print(f"--- Log for {self.name} ---")
        self.exchange_log.show()


desk = ExchangeDesk('Airport Kiosk')
desk.add_exchanger(USDToEUR())
desk.add_exchanger(USDToGBP())
desk.add_exchanger(USDToJPY())
desk.add_exchanger(CustomExchanger('USDToUZS', 12850.0))

desk.exchange_all(200)
print()
desk.exchange_all(75)
print()
desk.show_log()

try:
    e = Exchanger('test')
except TypeError:
    print('Cannot instantiate abstract class')
