class Symbol():
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type

class SymbolTable():
    def __init__(self):
        self.symbols = {}

    def put(self, name, symbol):
        self.symbols[name] = symbol

    def get(self, name):
        symbol = self.symbols[name]
        return symbol