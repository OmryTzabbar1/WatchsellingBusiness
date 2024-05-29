import json

from Watch import*

class Account:

    def __init__(self, firstName, lastName, username, password):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password
        self.watchUID = 0
        self.balance = None
        self.debt = None
        self.inventory = {}


    """*later problem* def buyWatch(self):
        
        with open(f'{self.firstName}_{self.lastName}_account_data.json', 'w') as file:
            json.dump(data, file)"""


    def Buy(self):
        #creates watch
        brand, model, price, UID = input("Enter brand name: "), input("Enter model: "), input("Enter purchase price"), \
                                   self.watchUID
        print('____________________________________________')
        cont = input("Do you want to continue inputting information? ")
        if cont.lower() == 'yes' or 'y':
            isConsigned, serialNumber, full_kit, year = input("Is this a consignment piece? "), \
                                                        input("Enter serial number: "), \
                                                        input("Full kit? "), \
                                                        input("Enter the year: ")
            self.inventory[UID] = Watch(brand, model, price, UID, isConsigned, serialNumber, full_kit, year)
        else:
            self.inventory[UID] = Watch(brand, model, price, UID)

        self.watchUID += 1


    def Sell(self, UID, soldPrice):
        if UID in self.inventory and not self.inventory[UID].isSold():
            self.inventory[UID].set_sold(True)
            self.balance += soldPrice
            print("The " + self.inventory[UID].get_brand() + " sold for $" + soldPrice)
        else:
            print("The watch either does not exist, or is already sold")


    def Trade(self, UID, args):
        pass
