from case import StandardCase, SouvenirCase, StickerCapsule
from cases import bravo_case
from cases import dreamhack_cobblestone
from cases import ems_katowice_2014_challengers

def main():
    #standard case test opening,
    bravo = StandardCase("Operation Bravo", bravo_case.items_by_rarity)
    souvenir_case = SouvenirCase("DreamHack 2014 Cobblestone Souvenir", dreamhack_cobblestone.items_by_rarity)
    capsule = StickerCapsule("EMS Katowice 2014 Challengers", ems_katowice_2014_challengers.items_by_rarity)

    print("Opening 5 Bravo Cases...\n")
    for i in range(5):
        item = bravo.open()
        if item is None:
            print("No item dropped.\n")
        else:
            print()

    #souvenir case test opening 
    print("Opening 5 DreamHack 2014 Cobblestone Souvenir Packages...\n")
    for _ in range(5):
        item = souvenir_case.open()
        if item:
            print()

    #sticker capsule case test opening
    print("Opening 5 EMS Katowice 2014 Challengers Sticker Capsules...\n")
    for _ in range(5):
        item = capsule.open()
        if item:
            print()

if __name__ == "__main__":
    main()