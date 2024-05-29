import json

class WatchBusiness:
    def __init__(self):
        self.load_data()

    def load_data(self):
        try:
            with open('watch_business_data.json', 'r') as file:
                data = json.load(file)
                self.available_money = data['available_money']
                self.total_sales = data['total_sales']
                self.total_spent = data['total_spent']
                self.watch_id = data['watch_id']
                self.inventory = data['inventory']

        except FileNotFoundError:
            # If the file doesn't exist, initialize with default values
            self.available_money = 10000
            self.total_sales = 0
            self.total_spent = 0
            self.watch_id = 0
            self.inventory = {}

    def save_data(self):
        data = {
            'available_money': self.available_money,
            'total_sales': self.total_sales,
            'total_spent': self.total_spent,
            'watch_id': self.watch_id,
            'inventory': self.inventory,
        }

        with open('watch_business_data.json', 'w') as file:
            json.dump(data, file)

    def buy_watch(self, quantity):

        for i in range(quantity):
            price = int(input("What was the price paid for the watch? "))
            brand = input("What's the name of the brand? ")
            model = input("What's the name of the model? ")

            self.watch_id += 1

            self.inventory[self.watch_id] = {'brand': brand, 'model': model, 'price': price}

            print(f"Successfully purchased {brand} {model}.")

            self.available_money -= price
            self.total_spent += price
            self.save_data()

    def sell_watch(self, watch_id, price):
        if watch_id not in self.inventory:
            print("Watch not available in sufficient quantity.")
            return

        self.available_money += price
        self.total_sales += price
        self.inventory[watch_id]['quantity'] = "SOLD!"

        print(f"Successfully sold {self.inventory[watch_id]['brand'], self.inventory[watch_id]['brand']}.")
        self.save_data()

    def trade_watch(self, giving_id, receiving_quantity, cash_quantity=0):
        for i in range(receiving_quantity):

            if giving_id not in self.inventory:
                print("Watch not available in sufficient quantity for trading.")
                return

            price = f"Part of a trade for {giving_id}"
            brand = input("What's the name of the brand? ")
            model = input("What's the name of the model? ")

            self.watch_id += 1

            # Update inventory for the given watch
            self.inventory[giving_id]['quantity'] = f'Traded for {self.watch_id} until {self.watch_id + receiving_quantity - 1}'

            # Add new watches to inventory
            self.inventory[self.watch_id] = {'brand': brand, 'model': model, 'price': price}

        print(f"Successfully traded {receiving_quantity} watch(s) + ${cash_quantity}. New watch ID(s): {1 + self.watch_id - receiving_quantity, self.watch_id}")
        self.save_data()

# Example usage
watch_business = WatchBusiness()
action = input('What would you like to do: ((1) Buy a Watch) ((2) Sell a Watch) ((3) Trade a Watch)')
if action == '1':
    quantity = int(input("How many watches are you buying? "))
    watch_business.buy_watch(quantity)
elif action == '2':
    watch_id = input("Enter the ref number: ")
    sale_price = int(input("Enter the sale price: "))
else:
    giving_id, receiving_quantity, cash_quantity = input(), input(), input()

watch_business.save_data()
