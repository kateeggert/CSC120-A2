from computer import *
from typing import Dict, Optional

class ResaleShop:
    
    """Attributes:"""
    inventory = []

    """ResaleShop creates a store inventory, and has methods that allow the shop to buy, sell, and refurbish computers."""
    
    """Constructor"""
    def __init__(self, inventory):
        self.inventory = inventory

    """Allows the shop to buy a computer by adding a new computer to the inventory"""
    def buy(self, comp):
        self.inventory.append(comp)
        return self.inventory

    """Sells a computer by removing the computer from the inventory, given that the computer exists in inventory"""
    def sell(self, comp):
        if comp in self.inventory:
            desc = comp.description
            print(f"{desc} sold")
            self.inventory.remove(comp)
            return self.inventory
        else: 
            print(f"{desc} not found. Please select another item to sell.")

    """Updates the price of the computer according to the year made and optionally updates the os, given that the computer is in inventory"""
    def refurbish(self, comp, new_os: Optional[str] = None):
        if comp in self.inventory: # locate the computer
            if int(comp.year_made) < 2000:
                Computer.update_price(comp, 0) # too old to sell, donation only
            elif int(comp.year_made) < 2012:
                Computer.update_price(comp, 250) # heavily-discounted price on machines 10+ years old
            elif int(comp.year_made) < 2018:
                Computer.update_price(comp, 550) # discounted price on machines 4-to-10 year old machines
            else:
                Computer.update_price(comp, 1000) # recent stuff

            if new_os is not None:
                Computer.update_os(comp, new_os) # update details after installing new OS
        else:
            print(f"{comp.description} not found. Please select another item to refurbish.")

def main():
    myShop: ResaleShop = ResaleShop(inventory = [])
    comp: Computer = Computer("Mac Pro (Late 2013)",
    "3.5 GHc 6-Core Intel Xeon E5", 1024, 64,
    "macOS Big Sur", 2013, 1500)
    myShop.buy(comp)
    print(comp.operating_system)
    print(comp.price)
    myShop.refurbish(comp, "MacOS Monterey")
    print(comp.operating_system)
    print(comp.price)
    myShop.sell(comp)
    

if __name__ == "__main__":
    main()

