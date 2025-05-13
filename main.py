from case import StandardCase, SouvenirCase, StickerCapsule
from cases import bravo_case
from cases import dreamhack_cobblestone
from cases import ems_katowice_2014_challengers
from CaseRegistry import * #registry for player input

def main():
    print("Welcome to cs gamble sim 10 million")
    print("Cases to choose from: bravo, katowice capsule, or cobblestone")
    print("Type 'quit' to exit at any time. \n")

    while True:
        case_name = input("Enter the name of the case you want to open: ").strip()
        if case_name.lower() in ("quit", "q"):
            print("Goodbye! Quitters never win.")
            break


        case = registry.get_case(case_name)

        if not case:
            print("Invalid case name.")
            continue
        
        try:
            count = int(input(f"How many {case_name} cases would you like to open? "))
        except ValueError:
            print("Invalid number.")
            continue
        
        print(f"\n Opening {count}x {case_name.title()}...\n")

        special_drops = []

        for _ in range(count):
            item, rarity = case.open()  # unpack both item and rarity
            if item:
                if hasattr(case, "best_rarity"):
                    # Support single or multiple rarities
                    if isinstance(case.best_rarity, (tuple, list)):
                        if rarity in case.best_rarity:
                            special_drops.append((item, rarity))
                    else:
                        if rarity == case.best_rarity:
                            special_drops.append((item, rarity))
                print()

        if special_drops:
            print("GIGA DROPS!!!!: ")
            for item, rarity in special_drops:
                print(f" * {item} ({rarity})")
        else:
            print("No top-tier items. Keep gambling.")

if __name__ == "__main__":
    main()