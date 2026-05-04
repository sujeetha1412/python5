class ElectricityBill:
    def __init__(self, name, units):
        self.name = name
        self.units = units
        self.amount = 0.0
    def calculate_bill(self):
        u = self.units
        if u <= 100:
            self.amount = 0.0
        elif u <= 200:
            self.amount = (u - 100) * 1.5
        elif u <= 300:
            self.amount = (100 * 1.5) + (u - 200) * 2.5
        elif u <= 400:
            self.amount = (100 * 1.5) + (100 * 2.5) + (u - 300) * 4
        else:
            self.amount = (100 * 1.5) + (100 * 2.5) + (100 * 4) + (u - 400) * 6
    def show_invoice(self):
        print("\n--- Electricity Bill ---")
        print("Customer Name: ", self.name)
        print("Units Used:    ", self.units)
        print("Total Bill:    Rs.", round(self.amount, 2))
n = int(input("Enter number of customers: "))
for i in range(n):
    print("\nEnter details for Customer ")
    c_name = input("Enter Customer Name: ")
    c_units = float(input("Enter Units Consumed: "))
    bill_obj = ElectricityBill(c_name, c_units)
    bill_obj.calculate_bill()
    bill_obj.show_invoice()
