import random
from config import RARITY_WEIGHT_STANDARD, RARITY_WEIGHT_SOUVENIR, RARITY_WEIGHT_STICKER_CAPSULE

class StandardCase:
    def __init__(self, name, items_by_rarity):
        self.name = name
        self.items_by_rarity = items_by_rarity
        self.best_rarity = "Exceedingly Rare"

    def open(self):
        rarities = list(RARITY_WEIGHT_STANDARD.keys())
        weights = list(RARITY_WEIGHT_STANDARD.values())
        chosen_rarity = random.choices(rarities, weights=weights, k=1)[0]

        pool = self.items_by_rarity.get(chosen_rarity, [])
        if not pool:
            print(f"No items available in rarity: {chosen_rarity}")
            return None
        
        item = random.choice(pool)
        print(f"[{self.name}] You unboxed: {item} ({chosen_rarity})")
        if chosen_rarity == self.best_rarity:
            print("GOLD GOLD GOLD GOLD")
        return item, chosen_rarity
    
class SouvenirCase:
    def __init__(self, name, items_by_rarity):
        self.name = name
        self.items_by_rarity = items_by_rarity
        self.best_rarity = ("Covert", "Classified")

    def open(self):
        rarities = list(RARITY_WEIGHT_SOUVENIR.keys())
        weights = list(RARITY_WEIGHT_SOUVENIR.values())
        chosen_rarity = random.choices(rarities, weights=weights, k=1)[0]

        pool = self.items_by_rarity.get(chosen_rarity, [])
        if not pool:
            print(f"No items available in rarity: {chosen_rarity}")
            return None
        
        item = random.choice(pool)
        print(f"[{self.name}] You unboxed: {item} ({chosen_rarity})")
        if chosen_rarity in self.best_rarity:
            print("GOLD GOLD GOLD GOLD")
        return item, chosen_rarity


class StickerCapsule:
    def __init__(self, name, items_by_rarity):
        self.name = name
        self.items_by_rarity = items_by_rarity
        self.best_rarity = ("Extraordinary", "Exotic")

    def open(self):
        rarities = list(RARITY_WEIGHT_STICKER_CAPSULE.keys())
        weights = list(RARITY_WEIGHT_STICKER_CAPSULE.values())
        chosen_rarity = random.choices(rarities, weights=weights, k=1)[0]

        pool = self.items_by_rarity.get(chosen_rarity, [])
        if not pool:
            print(f"No items available in rarity: {chosen_rarity}")
            return None, None

        item = random.choice(pool)
        print(f"[{self.name}] You unboxed: {item} ({chosen_rarity})")
        if chosen_rarity in self.best_rarity:
            print("GOLD GOLD GOLD GOLD")
        return item, chosen_rarity