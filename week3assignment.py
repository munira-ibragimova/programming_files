class LootDrop:
    def __init__(self, item_name: str, gold_value: float, count: int):
        self.item_name = item_name
        self.gold_value = gold_value
        self.count = count

    def __str__(self):    
        return f"{self.item_name}: {self.count} drop(s) worth ${self.gold_value}"
    
    def __repr__(self):
        return f"LootDrop('{self.item_name}', {self.gold_value}, {self.count})"
    
    def __add__(self, other):
        if isinstance(other, LootDrop):
            if self.item_name == other.item_name:
                return LootDrop(self.item_name, self.gold_value, self.count + other.count)
            return NotImplemented
        elif isinstance(other, int):
            return LootDrop(self.item_name, self.gold_value, self.count + other)        
        return NotImplemented
    
    def __eq__(self, value):
        if isinstance(value, LootDrop):
            return (self.item_name, self.gold_value) == (value.item_name, value.gold_value)
        return NotImplemented
    def __bool__(self):
        return self.count > 0
    


drop1 = LootDrop("Health Potion", 15.0, 3)
drop2 = LootDrop("Health Potion", 15.0, 2)
drop3 = LootDrop("Mana Potion", 20.0, 0)

print(str(drop1))
print(repr(drop1))
print(drop1 + drop2)
print(drop1 + 5)
print(drop1 == drop2)
print(bool(drop1))
print(bool(drop3))
