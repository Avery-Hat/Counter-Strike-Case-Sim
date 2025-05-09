import random

class CaseItem:
    def __init__(self, name):
        self.name = name
        self.wear_rate = round(random.uniform(0.00, 1.00), 4)
        self.condition = self.get_condition()

    def get_condition(self):
        if self.wear_rate <= 0.07:
            return "Factory New"
        if self.wear_rate <= 0.15:
            return "Minimal Wear"
        if self.wear_rate <= 0.38:
            return "Field-Tested"
        if self.wear_rate <= 0.45:
            return "Well-Worn"
        else:
            return "Battle-Scarred"
    
    def __str__(self):
        return f"{self.name} [{self.condition} | {self.wear_rate}]"

class StickerItem:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"