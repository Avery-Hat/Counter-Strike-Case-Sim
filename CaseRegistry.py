from case import StandardCase, SouvenirCase, StickerCapsule
from cases import bravo_case, dreamhack_cobblestone, ems_katowice_2014_challengers

class CaseRegistry:
    def __init__(self):
        self._cases = {}
    
    def register(self, aliases, case):
        for name in aliases:
            self._cases[name.lower()] = case
    
    def get_case(self, name):
        return self._cases.get(name.lower().strip())
   

#for cases with aliases:
registry = CaseRegistry()

registry.register(
    ["bravo", "operation bravo"], 
    StandardCase("Operation Bravo", bravo_case.items_by_rarity)
)

registry.register(
    ["cobblestone", "souvenir cobblestone", "dlore", "dragon lore"],
     SouvenirCase(
         "DreamHack 2014 Cobblestone Souvenir", 
        dreamhack_cobblestone.items_by_rarity
        )
)

registry.register(
    ["katowice", "challengers", "katowice 2014", "capsule", "katowice capsule"],
    StickerCapsule(
        "EMS Katowice 2014 Challengers Capsule", 
        ems_katowice_2014_challengers.items_by_rarity
        )
)