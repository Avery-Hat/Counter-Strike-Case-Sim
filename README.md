# Counter Strike 2 Case Simulator
A simulator for python3 terminal that lets you choose between 2 cases and a sticker capsule.
 * Bravo
 * DreamHack 2014 Cobblestone Souvenir Package (the beautiful Dragon Lore)
 * EMS Katowice 2014 Challengers Stickers (iBP Holo)

I chose the three classics due to their rarity, the fact that they hold the most prestige within the Counter-Strike community, and to create 3 different % values. The source for drop rates were taken from 3rd party websites listed within the code's comments.


# About
This is my first personal project for Boot.Dev. It took a bit of brainstorming but I wanted to integrate new ideas I had with OOP in mind. It's a concept that I wanted to grow within this project after cycling through some other ideas.


## Tools
Python3 via VSCode

## What I learned
Surprisingly, there aren't many coding projects that require user input or even creating them. It was fun utilizing basics such as those for the first time. A bit of time was also spent relearning python as I was stuck in C hell for the previous project before this.

### Registry
Like I said before, OOP was something I put a ton of focus into. The major meat of this was utilized in the registry file I created for inputs the player can use in order to open a case. UI will ask for a certain case to be opened, but I wanted it to be a bit more open ended
```py
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
```
I loved processing this information and pulling it back into main in order to make main.py feel a bit more neat and organized.


## Overview of main.py
```py
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
```

The majority of the heavy lifting was done and processed through my for loop and while True. The for loop was originally just processing the number of cases the user wanted to open and pasted it all out with spacing in between. Later I added additional information at the bottom: how many rare (expensive, low percentage) items were pulled.


# Enjoy!

I hope you enjoy pulling cases and perhaps even obtain some gambler's fallacy from pulling a knife within your first 5 pulls (I know I did). Learning new points of storage and processing information exactly where I wanted to was a blast learning, and I will continue with this project after the latest boot.dev event is complete. I'd like to add a visual UI from pygame, but that might be a while before it's fully realized. Cheers!



