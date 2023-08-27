class Customer:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.restaurants = []

    def given_name(self):
        return self.fname
    
    def set_given_name(self, new_given_name):
        self.fname = new_given_name

    def family_name(self):
        return self.lname
    
    def set_family_name(self, new_family_name):
        self.lname = new_family_name
    
    def full_name(self):
        return self.fname + " " + self.lname
    
    def add_restaurants(self, new_restaurant):
        self.restaurants.append(new_restaurant)

    def get_restaurants(self):
        return self.restaurants
    pass


customer = Customer("Ken", "Walibora")
print(customer.full_name())

customer.add_restaurants("Milan")
customer.add_restaurants("K1")
customer.add_restaurants("Brew Bistro")



print(customer.get_restaurants())
