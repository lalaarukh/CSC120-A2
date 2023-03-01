# set up for resaleshop
class ResaleShop:
    inventory = []
    name = ""
   
   #setting up attributes 

    def __init__(self, inventory, name):
        self.inventory = inventory
        self.name = name

    #set up the buy function: add it to computer
    def buy(self, computer):
        self.inventory.append(computer)

    #set up function to update price if in inventory and print warning if not
    def update_price(self, computer, new_price):
        if computer in self.inventory:
            self.new_price = new_price
        else:
            print(computer, "not found in inventory")

    #delete from inventory if selling a computer
    def sell(self, sell):
       # self.sell = sell
       if sell in self.inventory:
        del self.inventory
       else:
        print(sell, "not in inventory")

    #print invnetory if inventory is not 0
    def print_inventory(self):
        if len(self.inventory) != 0:
            print(self.inventory)
        else:
            print("No inventory to display")
        

    # example run

comp1 = ResaleShop([], "Lala")

comp1.buy("Macbok Air 2013")

comp1.buy("Macbook Air 2019")

comp1.sell("abcd")

comp1.print_inventory()