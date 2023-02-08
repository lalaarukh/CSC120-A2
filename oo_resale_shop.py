class ResaleShop:
    inventory = []
    name = ""
    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory, name):
        self.inventory = inventory
        self.name = name
        
    def buy(self, computer):
        self.inventory.append(computer)
        
    def update_price(self, computer, new_price):
        if computer in self.inventory:
            self.new_price = new_price
        else:
            print(computer, "not found in inventory")

    def sell(self, sell):
       # self.sell = sell
       if sell in self.inventory:
        del self.inventory
       else:
        print(sell, "not in inventory")

    def print_inventory(self):
        if len(self.inventory) != 0:
            print(self.inventory)
        else:
            print("No inventory to display")
        

    # What methods will you need?

comp1 = ResaleShop([], "Lala")

comp1.buy("Macbok Air 2013")

comp1.buy("Macbook Air 2019")

comp1.sell("abc")

comp1.print_inventory()